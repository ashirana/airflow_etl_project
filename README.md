# 🚀 Airflow ETL Pipeline Project

## 📌 Overview

This project demonstrates a complete ETL (Extract, Transform, Load) pipeline built using Apache Airflow, Docker, and PostgreSQL.

The pipeline extracts data from an API, transforms it, and loads it into a PostgreSQL database using Airflow DAG orchestration.

---

## 🏗️ Architecture

```
            +-------------------+
            |   Airflow DAG     |
            +-------------------+
                      |
        +--------------------------+
        |   Extract (API call)     |
        +--------------------------+
                      |
        +--------------------------+
        |   Transform (Clean Data) |
        +--------------------------+
                      |
        +--------------------------+
        |   Load (PostgreSQL)      |
        +--------------------------+
```

---

## ⚙️ Tech Stack

* Python
* Apache Airflow
* Docker & Docker Compose
* PostgreSQL
* psycopg2

---

## 📂 Project Structure

```
airflow_etl_project/
│
├── dags/
│   └── etl_pipeline.py
│
├── scripts/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## 🔄 Pipeline Flow

1. **Extract**

   * Fetch data from API
   * Save as JSON

2. **Transform**

   * Clean and structure data
   * Prepare for database load

3. **Load**

   * Insert data into PostgreSQL

---

## ▶️ How to Run

### 1. Start services

```bash
docker compose up
```

### 2. Open Airflow UI

```
http://localhost:8080
```

### 3. Login

```
Username: airflow
Password: airflow
```

### 4. Trigger DAG

* Enable DAG
* Click "Play" ▶️

---

## 🧪 Verification

Connect to PostgreSQL:

```bash
docker exec -it airflow_etl_project-postgres-1 psql -U airflow -d airflow
```

Run:

```sql
SELECT * FROM your_table LIMIT 10;
```

---

## ⚠️ Challenges Faced

* Module import errors inside Airflow containers
* Docker volume persistence issues
* Airflow user authentication setup
* XCom data passing debugging
* Handling missing keys in JSON (`KeyError`)

---

## 🚀 Future Improvements

* Add AWS S3 as data lake
* Use Spark for transformation
* Implement incremental loads
* Add logging & monitoring
* Use Airflow connections instead of hardcoded configs

---

## 🎯 Key Learnings

* Airflow DAG orchestration
* Debugging distributed systems
* ETL pipeline design
* Docker-based deployments

---

## 📌 Author

Ashish Ashish
