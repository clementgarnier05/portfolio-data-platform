FROM bitnami/spark:3

USER root

COPY spark-defaults.conf /opt/bitnami/spark/conf/spark-defaults.conf

RUN pip install --no-cache-dir \
      pyspark>=3.3.0 \
      delta-spark>=2.2.0

