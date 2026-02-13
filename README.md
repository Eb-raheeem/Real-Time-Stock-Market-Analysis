## Project Name: Real Time Stock Market Analysis

The project implements a real-time data pipeline that extracts stock data from Vantage API, streams it through Apache Kafka, processes it with Apache Spark, and loads it into a Postgres database.

All components are containerized with Docker for easy deployment.

### Data Pipeline Architecture
![Data Pipeline Architecture](./img/pipeline.svg)

Project Tech Stack and Flow
 - `Kafka UI - Inspect topics/messages.`
 - `API - produces JSON events into Kafka.`
 - `Spark - consumes from Kafka, writes to Postgres.`
 - `Postgres - stores results for analytics.`
 - `pgAdmin - manages Postgress visually.`
 - `PowerBI - external (connects to Postgres database).`

