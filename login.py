"""
This module defines the login blueprint for the Flask app.
"""
from flask import Blueprint
from flask import current_app as app
from flask import render_template

app_file1 = Blueprint("login", __name__, template_folder="templates")


@app_file1.route("/login")
def login():
    """
    Handle the /login route.

    Returns:
        A rendered HTML template.
    """
    user = "Kaushik"
    app.logger.info(f"User: { user } Logged in Successfully")
    return render_template("login/login.html", user="kaushik")
