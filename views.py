from flask import Blueprint, render_template, request

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    args = request.args
    uuid = args.get("uuid")
    return render_template("index.html", uuid=uuid)