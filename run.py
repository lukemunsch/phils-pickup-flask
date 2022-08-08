import os
import json
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    print ("Hello from python!")
    

if __name__ == "__name__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5500")),
        debug=True
    )