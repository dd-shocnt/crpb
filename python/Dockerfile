FROM python:3.10-slim
COPY --from=datadog/serverless-init:1 /datadog-init /app/datadog-init
ENV PYTHONUNBUFFERED True
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

ENV DD_SERVICE=cloudrun-python
ENV DD_ENV=su-cloudrun

ENTRYPOINT ["/app/datadog-init"]
CMD ["ddtrace-run", "python", "app.py"]
