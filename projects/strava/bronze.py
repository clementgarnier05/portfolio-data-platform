# bronze.py
import time
import json
import requests
from pyspark.sql import SparkSession
from pyspark.sql.functions import lit
from delta import configure_spark_with_delta_pip
from strava_auth import get_access_token, update_strava_tokens
import os

builder = (
    SparkSession.builder
        .appName("StravaBronze")
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
        .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
        .config("spark.hadoop.fs.s3a.metrics.publisher.factory", "org.apache.hadoop.fs.s3a.metrics.NullMetricsPublisher")
        .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
        .config("spark.hadoop.fs.s3a.aws.credentials.provider", "com.amazonaws.auth.profile.ProfileCredentialsProvider")
)
spark = configure_spark_with_delta_pip(builder).getOrCreate()

print("CLASSPATH DRIVER =", spark.sparkContext._conf.get("spark.driver.extraClassPath", "non défini"))
print("JARS dans jars :", spark.sparkContext._jsc.sc().listJars())
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

env = os.getenv("ENV", "staging")
bucket = f"s3a://portfolio-data-lake/{env}/bronze/strava_activities"
df_bronze.write.format("delta").mode("append").save(bucket)

spark.stop()
print("[bronze] Ingestion terminée.")