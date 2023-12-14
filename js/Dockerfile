FROM node:16-slim
RUN apt-get update
RUN apt-get install -y ca-certificates
WORKDIR /app
COPY package.json /app
COPY package-lock.json /app
RUN npm ci --only=production
COPY app.js /app/
COPY --from=datadog/serverless-init /datadog-init /app/datadog-init

ENV NODE_OPTIONS="--require dd-trace/init"
ENV DD_SERVICE=cloudrun-js
ENV DD_ENV=su-cloudrun

ENTRYPOINT ["/app/datadog-init"]
CMD ["npm", "run", "start"]
#CMD ["node", "/app/app.js"]
