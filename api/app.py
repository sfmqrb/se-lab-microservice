# app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Backend service is up and running."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

