FROM spark-base:latest

USER root

RUN pip install --upgrade pip \
 && pip install delta-spark>=4.0.0

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt


WORKDIR /app
COPY . /app

ENTRYPOINT ["spark-submit"]
CMD ["--master", "spark://spark-master:7077", "/app/bronze.py"]