FROM python:3.10-slim
COPY --from=datadog/serverless-init:1 /datadog-init /app/datadog-init
ENV PYTHONUNBUFFERED True
WORKDIR /app
COPY requirements.txt app.py /app/
RUN pip install --no-cache-dir -r requirements.txt

ENV DD_SERVICE=cloudrun-python
ENV DD_ENV=su-cloudrun
ENV DD_VERSION=1.0.0

ENTRYPOINT ["/app/datadog-init"]
CMD ["ddtrace-run", "python", "app.py"]
