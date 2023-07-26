from flask import Blueprint
from flask import render_template


app_file2 = Blueprint("logout", __name__, template_folder="templates")


@app_file2.route("/logout")
def returnJsonLogout():
    return render_template("logout/logout.html", user="Kaushik")
