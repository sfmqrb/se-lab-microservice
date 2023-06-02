from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def hello():
    return "Backend service is up and running."


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
