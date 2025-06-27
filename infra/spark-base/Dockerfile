FROM bitnami/spark:4.0.0-debian-12-r0
USER root

RUN apt-get update && \
    apt-get install -y --no-install-recommends curl ca-certificates && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir -p /opt/bitnami/spark/conf \
 && touch /opt/bitnami/spark/conf/hadoop-metrics2.properties

COPY core-site.xml /opt/bitnami/spark/conf/
COPY spark-defaults.conf /opt/bitnami/spark/conf/

RUN pip install --no-cache-dir pyspark>=3.4.0 \
 && pip install --no-cache-dir delta-spark==4.0.0 \
 && mkdir -p /opt/bitnami/spark/jars \
 && cd /opt/bitnami/spark/jars \
 && curl -sSL -O https://repo1.maven.org/maven2/io/delta/delta-spark_2.13/4.0.0/delta-spark_2.13-4.0.0.jar \
 && curl -fSL -O https://repo1.maven.org/maven2/io/delta/delta-storage/4.0.0/delta-storage-4.0.0.jar \
 && curl -sSL -O https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.3.4/hadoop-aws-3.3.4.jar \
 && curl -sSL -O https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.12.274/aws-java-sdk-bundle-1.12.274.jar

