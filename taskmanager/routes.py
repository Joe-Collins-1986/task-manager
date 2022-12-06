from flask import render_template, redirect, request, url_for
from taskmanager import app, db
from taskmanager.models import Catagory, Task


@app.route("/")
def home():
    return render_template("tasks.html")


@app.route("/catagories")
def catagories():
    catagories = list(Catagory.query.order_by(Catagory.catagory_name).all())
    return render_template("catagories.html", catagories=catagories)


@app.route("/add_catagory", methods=["GET", "POST"])
def add_catagory():
    if request.method == "POST":
        catagory = Catagory(catagory_name=request.form.get("catagory_name"))
        db.session.add(catagory)
        db.session.commit()
        return redirect(url_for("catagories"))
    return render_template("add_catagory.html")


@app.route("/edit_catagory/<int:catagory_id>", methods=["GET", "POST"])
def edit_catagory(catagory_id):
    catagory = Catagory.query.get_or_404(catagory_id)
    if request.method == "POST":
        catagory.catagory_name = request.form.get("catagory_name")
        db.session.commit()
        return redirect(url_for("catagories"))
    return render_template("edit_catagory.html", catagory=catagory)


@app.route("/delete_catagory/<int:catagory_id>")
def delete_catagory(catagory_id):
    catagory = Catagory.query.get_or_404(catagory_id)
    db.session.delete(catagory)
    db.session.commit()
    return redirect(url_for("catagories"))
