from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)


@app.route("/")
def home():
    return "Hey Hello from Flask SIde"


@app.route("/path_of_response", methods=["GET"])
def returnJson():
    if request.method == "GET":
        data = {
            "Modules": 15,
            "Subject": "Data Structures and Algorithms",
        }

        return jsonify(data)


@app.route("/map", methods=["GET"])
def returnJsonMap():
    if request.method == "GET":
        data = {
            "Modules": 19,
            "Subject": "Computer Networking",
        }

        return jsonify(data)


@app.route("/second", methods=["GET"])
def returnJsonSecond():
    if request.method == "GET":
        data = {
            "Modules": 20,
            "Subject": "Computer Architechture",
        }

        return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
