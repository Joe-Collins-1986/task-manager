from flask import render_template, redirect, request, url_for
from taskmanager import app, db
from taskmanager.models import Catagory, Task


@app.route("/")
def home():
    tasks = list(Task.query.order_by(Task.id).all())
    return render_template("tasks.html", tasks=tasks)


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


@app.route("/add_task", methods=["GET", "POST"])
def add_task():
    catagories = list(Catagory.query.order_by(Catagory.catagory_name).all())
    if request.method == "POST":
        task = Task(
            task_name=request.form.get("task_name"),
            task_description=request.form.get("task_description"),
            is_urgent=bool(True if request.form.get("is_urgent") else False),
            due_date=request.form.get("due_date"),
            catagory_id=request.form.get("catagory_id")
        )
        db.session.add(task)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add_task.html", catagories=catagories)


@app.route("/edit_task/<int:task_id>", methods=["GET", "POST"])
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    catagories = list(Catagory.query.order_by(Catagory.catagory_name).all())
    if request.method == "POST":
        task.task_name = request.form.get("task_name")
        task.task_description = request.form.get("task_description")
        task.is_urgent = bool(True if request.form.get("is_urgent") else False)
        task.due_date = request.form.get("due_date")
        task.catagory_id = request.form.get("catagory_id")
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit_task.html", task=task, catagories=catagories)


@app.route("/delete_task/<int:task_id>")
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("home"))