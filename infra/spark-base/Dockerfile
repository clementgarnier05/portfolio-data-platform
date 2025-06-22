FROM bitnami/spark:3
USER root

COPY core-site.xml /opt/bitnami/spark/conf/core-site.xml
COPY spark-defaults.conf /opt/bitnami/spark/conf/spark-defaults.conf

RUN pip install --no-cache-dir pyspark>=3.3.0 \
 && mkdir -p /opt/bitnami/spark/jars \
 && cd /opt/bitnami/spark/jars \
 && curl -sSLO https://repo1.maven.org/maven2/io/delta/delta-spark_2.12/4.0.0/delta-spark_2.12-4.0.0.jar

