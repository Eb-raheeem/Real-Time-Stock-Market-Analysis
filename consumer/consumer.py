from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, TimestampType
from pyspark.sql.functions import from_json, col
import os

# directory where spark will store it's checkpoint data. crucial in streaming to enable fault tolerance
checkpoint_dir = "tmp/checkpoint/Kafka_to_postgres"
if not os.path.exists(checkpoint_dir):
    os.makedirs(checkpoint_dir)


postgres_config = {
    "url": "jdbc:postgresql://postgres:5432/stock_data",
    "user": "admin",
    "password": "admin",
    "dbtable": "stocks",
    "driver": "org.postgresql.Driver"
}

# The schema/structure matching the new data coming from kafka
Kafka_data_schema = StructType([
    StructField("date", StringType()),
    StructField("high", StringType()),
    StructField("low", StringType()),
    StructField("open", StringType()),
    StructField("close", StringType()),
    StructField("symbol", StringType()),
])

spark = (SparkSession.builder
         .appName('KafkaSparkstreaming')
         .getOrCreate()
         )

df = (spark.readStream.format('kafka')
      .option('Kafka.bootstrap.servers', 'kafka:9092')
      .option('subscribe', 'stock_analysis')
      .option('startingOffsets', 'latest')  # Read only new incoming messages
      # if kafka delets old messages (rentention)
      .option('failOnDataLoss', 'false')
      .load()  # start reading the kafka topic as a stream
      )

# convert the 'value' column (which is a json string) into structured columns
parsed_df = df.selectExpr('CAST(value AS STRING)') \
    .select(from_json(col("value"), Kafka_data_schema).alias("data")) \
    .select("data.*")

processed_df = parsed_df.select(
    col("date").cast(TimestampType()).alias("date"),
    col("high").alias("high"),
    col("low").alias("low"),
    col("open").alias("open"),
    col("close").alias("close"),
    col("symbol").alias("symbol")
)

# display the results to the terminal (console output mode) ----Testing
"""
query = processed_df.writeStream \
    .outputMode("append") \
    .format("console") \
    .option("truncate", "false") \
    .option("checkpointLocation", checkpoint_dir) \
    .start()
"""

# Writes a microbatch dataframe to postgresql using JDBC in 'append' mode.


def write_to_postgres(batch_df, batch_id):
    batch_df.write \
        .format("jdbc") \
        .mode("append") \
        .options(**postgres_config) \
        .save()


# ----- stresam to postgresql using foreachBatch
query = (
    processed_df.writeStream
    .foreachBatch(write_to_postgres)
    .option('checkpointLocation', checkpoint_dir)
    .outputMode('append')
    .start()
)


# run indefinetly unless terminated
query.awaitTermination()
