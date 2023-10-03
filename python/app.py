import os
from flask import Flask, Response

app = Flask(__name__)
msg = "Hello world from su-cloudrun-python " + os.environ.get("DD_VERSION")

@app.route("/")
def home():
    return Response("{\"msg\": msg}", status=200, mimetype='application/json')

app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
