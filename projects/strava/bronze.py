# bronze.py
import time
import json
import requests
from pyspark.sql import SparkSession
from pyspark.sql.functions import lit

from strava_auth import get_access_token, update_strava_tokens

spark = (
    SparkSession.builder
    .appName("StravaBronze")
    .config("spark.jars.packages", "io.delta:delta-core_2.12:2.2.0")
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
    .getOrCreate()
)

update_strava_tokens()
token = get_access_token()

all_acts = []
page = 1
while True:
    resp = requests.get(
        "https://www.strava.com/api/v3/athlete/activities",
        headers={"Authorization": f"Bearer {token}"},
        params={"page": page, "per_page": 200}
    )
    resp.raise_for_status()
    batch = resp.json()
    if not batch:
        break
    all_acts.extend(batch)
    print(f"[bronze] Page {page} → {len(batch)} activités")
    page += 1
    time.sleep(1)

df_raw = spark.read.json(spark.sparkContext.parallelize(all_acts))

df_bronze = df_raw.withColumn("_ingest_timestamp", lit(int(time.time())))

bronze_path = "/data/bronze/strava_activities"
df_bronze.write.format("delta").mode("append").save(bronze_path)

spark.stop()
print("[bronze] Ingestion terminée.")