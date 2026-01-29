from flask import Blueprint, render_template, request

user = Blueprint("user", __name__)

@user.route("/profile")
def profile():
    return "This the profile section"