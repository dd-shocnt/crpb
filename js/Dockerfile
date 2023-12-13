FROM node:16
WORKDIR /app
COPY package.json /app
COPY package-lock.json /app
RUN npm ci --only=production
COPY app.js /app/
COPY --from=datadog/serverless-init:1 /datadog-init /app/datadog-init

ENV NODE_OPTIONS="--require dd-trace/init"
ENV DD_SERVICE=cloudrun-js
ENV DD_ENV=su-cloudrun

ENTRYPOINT ["/app/datadog-init"]
CMD ["npm", "run", "start"]
