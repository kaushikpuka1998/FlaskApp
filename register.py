"""
This module defines the logout blueprint for the Flask app.
"""
from flask import Blueprint  # pylint: disable=import-error
from flask import render_template  # pylint: disable=import-error


app_file3 = Blueprint("register", __name__, template_folder="templates")


@app_file3.route("/register")
def return_json_logout():
    """
    Handle the /register route.

    Returns:
        A rendered HTML template.
    """
    return render_template("register/register.html", user="Kaushik")
