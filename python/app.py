import os
from flask import Flask, Response, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", version=os.environ.get("DD_VERSION"))
    
app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
