from flask import Blueprint, render_template, request

admin = Blueprint("admin", __name__)

@admin.route("/admin")
def adminDashboard():
    return "This is the admin landing page"