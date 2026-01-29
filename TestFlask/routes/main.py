from flask import Blueprint, render_template, request
from db import get_connection
main = Blueprint("main", __name__)


@main.route("/add-user", methods=["GET", "POST"])
def addUser():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]

        conn = get_connection()
        conn.execute("INSERT INTO users (username, email) VALUES (?, ?)", (username, email))
        conn.commit()
        conn.close()

        return "User saved to database!"

    return render_template("addUser.html")

@main.route("/")
def home():
    return render_template("home.html")

@main.route("/about")
def about():
    return render_template("about.html")

@main.route("/contact")
def contact():
    return render_template("contact.html")

@main.route("/form", methods = ["GET", "POST"])
def form():
    if request.method == "POST":
        username = request.form["username"]
        return f"Hello {username}!"
    return render_template("form.html")

@main.route("/services")
def services():
    return "service landing page"