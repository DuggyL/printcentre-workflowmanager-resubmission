from flask import (
    Flask, flash, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from workflowmanager import app, mongo

@app.route("/")
@app.route("/get_tasks")
def get_tasks():
    tasks = list(mongo.db.tasks.find())
    return render_template("tasks.html", tasks=tasks)

@app.route("/add_task", methods=["GET", "POST"])
def add_task():
    if request.method == "POST":
        is_urgent = "on" if request.form.get("urgent") else "off"
        task = {
            "job_title": request.form.get("job_title"),
            "company_name": request.form.get("company_name"),
            "job_description": request.form.get("job_description"),
            "quantity": request.form.get("quantity"),
            "materials": request.form.get("materials"),
            "printing": request.form.get("printing"),
            "finishing": request.form.get("finishing"),
            "delivery": request.form.get("delivery"),
            "delivery_date": request.form.get("delivery_date"),
            "delivery_address": request.form.get("delivery_address"),
            "urgent": is_urgent,
            "created_by": session["user"]
        }
        mongo.db.tasks.insert_one(task)
        flash("Task Successfully Added", category='success')
        return redirect(url_for("get_tasks"))
    customers = list(Customer.query.order_by(Customer.company_name).all())
    return render_template("add_task.html", customers=customers)