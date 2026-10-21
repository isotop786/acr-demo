from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello from New ACR Demo for Task v33.0 for ACR Build!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)