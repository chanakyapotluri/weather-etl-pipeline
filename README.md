\# Weather ETL Pipeline



\## Project Overview

This project is a beginner-friendly data engineering pipeline that extracts live weather data from a public weather API, stores the raw data locally, loads it into PostgreSQL, and runs SQL analytics on top of the collected data.



The goal of this project is to demonstrate an end-to-end ETL workflow using Python, PostgreSQL, and SQL.



\## Tech Stack

\- Python

\- PostgreSQL

\- SQLAlchemy

\- Pandas

\- Requests

\- python-dotenv

\- SQL

\- Git/GitHub



\## Pipeline Flow

1\. Extract weather data from a public API

2\. Convert JSON response into structured tabular data

3\. Save raw weather data as CSV

4\. Load weather data into PostgreSQL

5\. Run SQL analytics on the stored data



\## Project Structure

```text

weather-data-pipeline/

│

├── data/

│   ├── raw/

│   └── processed/

│

├── scripts/

│   ├── fetch\_weather.py

│   ├── load\_weather\_to\_db.py

│   └── test\_db\_connection.py

│

├── sql/

│   └── weather\_analytics.sql

│

├── notebooks/

│

├── README.md

├── requirements.txt

└── .gitignore
```



Database Table

Table name: raw_weather

Columns:

  id
  city
  temperature_c
  humidity
  weather_desc
  observation_time
  loaded_at

Example Analytics Query

SELECT
    city,
    AVG(temperature_c) AS avg_temperature_c,
    AVG(humidity) AS avg_humidity,
    COUNT(*) AS total_records
FROM raw_weather
GROUP BY city;

What This Project Demonstrates

  API data extraction
  JSON parsing
  Python data processing
  PostgreSQL database loading
  Environment variable usage
  SQL analytics
  Git/GitHub project workflow

Future Improvements

  Add logging
  Add data validation
  Create processed tables
  Add dbt transformations
  Add Airflow orchestration
  Store raw files in AWS S3
  Build dashboard using Power BI or Streamlit

