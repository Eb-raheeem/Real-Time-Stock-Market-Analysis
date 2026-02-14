from kafka import KafkaConsumer
import json
import time

# -- Configuration matching the producer ----
consumer = KafkaConsumer(
    'stock_analysis',
    bootstrap_servers='localhost:9094',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-consumer-group',  # Define a consumer group
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("Start Kafka consumer. Waiting for messages on the topic 'stock_analysis'...")

for message in consumer:
    data = message.value

    # print the received data
    print(f" value (Deserialized): {data}")

consumer.close()
print("Kafka consumer closed")
