"""
This module defines the logout blueprint for the Flask app.
"""
from flask import Blueprint  # pylint: disable=import-error
from flask import render_template  # pylint: disable=import-error


app_file2 = Blueprint("logout", __name__, template_folder="templates")


@app_file2.route("/logout")
def return_json_logout():
    """
    Handle the /logout route.

    Returns:
        A rendered HTML template.
    """
    return render_template("logout/logout.html", user="Kaushik")
