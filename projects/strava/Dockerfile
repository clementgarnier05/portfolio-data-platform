FROM spark-base:latest

USER root

COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt

USER 1001

WORKDIR /app
COPY . /app

ENTRYPOINT ["bash","-c"]