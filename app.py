"""
This module defines the Flask app and registers the
login and logout blueprints.
"""
from flask import Flask  # pylint: disable=import-error

from login import app_file1  # pylint: disable=import-error
from logout import app_file2  # pylint: disable=import-error
from register import app_file3  # pylint: disable=import-error

app = Flask(__name__)

app.register_blueprint(app_file1)
app.register_blueprint(app_file2)
app.register_blueprint(app_file3)

# @app.route("/")
# def home():
#     return "Hey Hello from Flask SIde"


# @app.route("/path_of_response", methods=["GET"])
# def returnJson():
#     if request.method == "GET":
#         data = {
#             "Modules": 15,
#             "Subject": "Data Structures and Algorithms",
#         }

#         return jsonify(data)


# @app.route("/map", methods=["GET"])
# def returnJsonMap():
#     if request.method == "GET":
#         data = {
#             "Modules": 19,
#             "Subject": "Computer Networking",
#         }

#         return jsonify(data)


# @app.route("/second", methods=["GET"])
# def returnJsonSecond():
#     if request.method == "GET":
#         data = {
#             "Modules": 20,
#             "Subject": "Computer Architechture",
#         }

#         return jsonify(data)


# @app.route("/logout")
# def returnJsonLogout():
#     return render_template("logout.html", user="Kaushik")


if __name__ == "__main__":
    app.run(debug=True)
