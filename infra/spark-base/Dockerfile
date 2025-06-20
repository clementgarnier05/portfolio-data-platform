FROM bitnami/spark:3

USER root

COPY core-site.xml /opt/bitnami/spark/conf/core-site.xml

RUN pip install --no-cache-dir \
      pyspark>=3.3.0 \
      delta-spark>=2.2.0

