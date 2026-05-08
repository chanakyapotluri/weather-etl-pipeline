import subprocess
import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

try:
    logging.info("Starting Weather ETL Pipeline")

    subprocess.run(
        [sys.executable, "scripts/load_weather_to_db.py"],
        check=True
    )

    logging.info("Pipeline completed successfully")

except Exception as e:
    logging.error("Pipeline failed")
    logging.error(e)