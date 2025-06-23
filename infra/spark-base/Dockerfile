FROM bitnami/spark:4.0.0-debian-12-r0

USER root

RUN apt-get update && \
    apt-get install -y --no-install-recommends curl && \
    rm -rf /var/lib/apt/lists/*

COPY core-site.xml /opt/bitnami/spark/conf/core-site.xml
COPY spark-defaults.conf /opt/bitnami/spark/conf/spark-defaults.conf

RUN pip install --no-cache-dir pyspark>=3.4.0 && \
    mkdir -p /opt/bitnami/spark/jars && \
    cd /opt/bitnami/spark/jars && \
    curl -sSLO https://repo1.maven.org/maven2/io/delta/delta-spark_2.12/4.0.0/delta-spark_2.12-4.0.0.jar
