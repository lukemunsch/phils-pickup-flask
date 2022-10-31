"""set up app imports"""
import os
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    """Set up directory for index page"""
    return render_template("index.html")



@app.route("/contact_us")
def contact_us():
    """Set up directory for contact page"""
    return render_template("contact_us.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
