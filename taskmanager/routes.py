from flask import render_template, redirect, request, url_for
from taskmanager import app, db
from taskmanager.models import Catagory, Task


@app.route("/")
def home():
    return render_template("tasks.html")


@app.route("/catagories")
def catagories():
    return render_template("catagories.html")


@app.route("/add_catagory", methods=["GET", "POST"])
def add_catagory():
    if request.method == "POST":
        catagory = Catagory(catagory_name=request.form.get("catagory_name"))
        db.session.add(catagory)
        db.session.commit()
        return redirect(url_for("catagories"))
    return render_template("add_catagory.html")
