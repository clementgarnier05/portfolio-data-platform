FROM bitnami/spark:3

USER root

RUN pip install --no-cache-dir \
      pyspark>=3.3.0 \
      delta-spark>=2.2.0

USER 1001