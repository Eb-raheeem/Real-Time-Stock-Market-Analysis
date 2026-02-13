# 📈 Real-Time Stock Market Insights & Reporting

## 🏢 Business Context

MarketPulse Analytics, headquartered in New York, USA, provides institutional investors with real-time financial analytics and trading insights. As demand for ultra-low latency analytics grows, especially during peak trading windows such as market open and earnings releases—the company faces challenges around scalability, availability, and processing speed.

This project addresses those challenges by building a scalable, containerized real-time data pipeline capable of streaming, processing, and storing stock market data with minimal latency.

---

## 🎯 Project Objective

The goal of this project is to design and implement a scalable, fault-tolerant real-time data pipeline that:

- Collects live stock market data from financial APIs  
- Streams events through Apache Kafka (KRaft mode)  
- Processes streaming data using Apache Spark  
- Stores transformed data in PostgreSQL  
- Enables downstream analytics and dashboard reporting (Power BI)  

The system ensures MarketPulse can deliver reliable, low-latency financial insights to hedge funds, asset managers, and electronic brokers.

---

## 🏗 Architecture Overview

![Data Pipeline Architecture](./img/pipeline.svg)

### 🔄 End-to-End Data Flow

1. **Stock API (Alpha Vantage)**  
   - Fetches real-time stock price data  
   - Produces JSON events  

2. **Kafka (Streaming Layer)**  
   - Buffers and distributes stock events  
   - Enables decoupled, fault-tolerant streaming  

3. **Spark Structured Streaming**  
   - Consumes events from Kafka  
   - Performs transformation & enrichment  
   - Writes processed results to Postgres  

4. **Postgres (Storage Layer)**  
   - Stores curated stock metrics  
   - Serves as analytics-ready data store  

5. **Analytics Layer**  
   - Power BI connects to Postgres  
   - Real-time dashboards visualize trends and metrics  

---

## 🧰 Tech Stack

| Component      | Purpose |
|----------------|---------|
| Apache Kafka   | Real-time streaming backbone |
| Apache Spark   | Stream processing & transformation |
| PostgreSQL     | Analytical data storage |
| Docker         | Containerization & reproducibility |
| Kafka UI       | Topic & message inspection |
| pgAdmin        | Database management |
| Power BI       | Business intelligence dashboards |

---

## 🚀 Expected Outcomes

- Low-latency ingestion and processing  
- Distributed compute model using Spark workers  
- Interactive dashboards for stock price trends, trading volumes, moving averages, and price volatility  
- Operational efficiency with containerized microservices  
- Faster decision-making for institutional traders  

---

## 🐳 Running the Project

### Start the Stack

```bash
docker compose up -d
```

### Stop the Stack

```bash
docker compose down
```

---

## 🌐 Service Access

| Service           | URL / Port            |
|------------------|-----------------------|
| Spark Master UI  | http://localhost:8081 |
| Kafka UI         | http://localhost:8085 |
| PostgreSQL       | localhost:5434        |
| pgAdmin          | http://localhost:5050 |

---

## 🔗 Connection Details

### Spark
- Master URL: `spark://spark-master:7077`
- Web UI: `http://localhost:8081`

### Kafka
- External (host machine): `localhost:9094`
- Internal (Docker network): `kafka:9092`

### PostgreSQL
- Host: `localhost`
- Port: `5434`
- Database: `$POSTGRES_DB`
- Username: `$POSTGRES_USER`
- Password: `$POSTGRES_PASSWORD`

> **Note:** Check `.env` or `docker-compose.yml` for actual credentials when running locally.

---

## 📊 Web Interfaces

- **Spark Master UI:** Monitor jobs, executors, and cluster resources → http://localhost:8081  
- **Kafka UI:** Browse topics, messages, and consumer groups → http://localhost:8085  
- **pgAdmin:** Database management → http://localhost:5050  

> Credentials are set in `compose.yml`.

---

## 🧱 Architecture Summary

Kafka → Spark Streaming → PostgreSQL

- Kafka handles real-time ingestion.  
- Spark processes streaming data.  
- PostgreSQL stores processed results.  

This setup enables real-time analytics and dashboards for financial stock data.
