SELECT
    city,
    AVG(temperature_c) AS avg_temperature_c,
    AVG(humidity) AS avg_humidity,
    COUNT(*) AS total_records
FROM raw_weather
GROUP BY city;