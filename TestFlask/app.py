from flask import Flask, render_template, request
from db import get_connection

app = Flask(__name__)

@app.route("/")
def home():
    return "<a href='/add-user'>Add User</a> | <a href='/users'>View Users</a>"

@app.route("/add-user", methods=["GET", "POST"])
def add_user():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]

        if not username or not email:
            return "Fill all fields!"

        conn = get_connection()
        conn.execute(
            "INSERT INTO users (username, email) VALUES (?, ?)",
            (username, email)
        )
        conn.commit()
        conn.close()

        return "User saved successfully!"

    return render_template("addUser.html")


@app.route("/users")
def users():
    conn = get_connection()
    users = conn.execute("SELECT * FROM users").fetchall()
    conn.close()

    return render_template("users.html", users=users)


if __name__ == "__main__":
    app.run(debug=True)
