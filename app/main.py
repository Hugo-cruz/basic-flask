from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"
@app.route("/balance", methods=['GET'])
def balance():
    return "balance"


@app.route("/event", methods=['POST'])
def event():
    return "event"
