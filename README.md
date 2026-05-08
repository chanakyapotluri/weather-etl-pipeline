# Weather ETL Pipeline

An end-to-end ETL pipeline that extracts live weather data from a public API, stores raw data locally, loads it into PostgreSQL, and runs SQL analytics on top of the collected data.

---

## Pipeline Architecture

```
Weather API → Python Extraction → Raw CSV Storage → PostgreSQL → SQL Analytics
```

---

## Tech Stack

- **Python** — data extraction, transformation, and loading
- **PostgreSQL** — relational database for structured storage
- **SQLAlchemy** — database connection and ORM
- **Pandas** — data transformation and structuring
- **Requests** — API calls
- **python-dotenv** — environment variable management
- **SQL** — analytics queries

---

## Pipeline Flow

1. **Extract** — Fetch live weather data from a public REST API
2. **Transform** — Parse JSON response into structured tabular format using Pandas
3. **Store Raw** — Save raw data as CSV for auditability and reprocessing
4. **Load** — Insert structured data into PostgreSQL
5. **Analyze** — Run SQL analytics queries on stored data

---

## Project Structure

```
weather-etl-pipeline/
│
├── data/
│   ├── raw/                   # Raw CSV files from API
│   └── processed/             # Transformed data
│
├── scripts/
│   ├── fetch_weather.py       # API extraction logic
│   ├── load_weather_to_db.py  # PostgreSQL loading logic
│   └── test_db_connection.py  # Connection validation
│
├── sql/
│   └── weather_analytics.sql  # Analytics queries
│
├── notebooks/                 # Exploratory analysis
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Database Schema

**Table:** `raw_weather`

| Column | Type | Description |
|---|---|---|
| id | SERIAL | Primary key |
| city | VARCHAR | City name |
| temperature_c | FLOAT | Temperature in Celsius |
| humidity | FLOAT | Humidity percentage |
| weather_desc | VARCHAR | Weather description |
| observation_time | TIMESTAMP | Time of observation |
| loaded_at | TIMESTAMP | Time data was loaded into DB |

---

## Example Analytics Query

```sql
SELECT
    city,
    AVG(temperature_c)  AS avg_temperature,
    AVG(humidity)       AS avg_humidity,
    COUNT(*)            AS total_records
FROM raw_weather
GROUP BY city
ORDER BY avg_temperature DESC;
```

---

## What This Project Demonstrates

- End-to-end ETL pipeline design and implementation
- REST API data extraction and JSON parsing
- Data transformation using Pandas
- PostgreSQL schema design and data loading
- Environment variable management for secure credentials
- SQL analytics on structured data
- Clean project structure following data engineering best practices

---

## Roadmap

- [ ] Add structured logging
- [ ] Add data validation layer
- [ ] Build processed/aggregated tables
- [ ] Integrate dbt for transformation layer
- [ ] Orchestrate with Apache Airflow
- [ ] Store raw files in AWS S3
- [ ] Build dashboard with Streamlit or Power BI

---

## Setup & Usage

1. Clone the repository
```bash
git clone https://github.com/chanakyapotluri/weather-etl-pipeline.git
cd weather-etl-pipeline
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Configure environment variables
```bash
cp .env.example .env
# Add your API key and PostgreSQL credentials
```

4. Run the pipeline
```bash
python scripts/fetch_weather.py
python scripts/load_weather_to_db.py
```

5. Run analytics
```bash
psql -d your_db_name -f sql/weather_analytics.sql
```

---

## Connect

**LinkedIn:** [Chanakya Potluri](https://www.linkedin.com/in/potluri-chanakya)  
**Portfolio:** [chanakya-potluri-portfolio.vercel.app](https://chanakya-potluri-portfolio.vercel.app)