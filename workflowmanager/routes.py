from flask import (
    Flask, flash, render_template, redirect, request, session, url_for)
#from flask_pymongo import PyMongo
#from bson.objectid import ObjectId
#from werkzeug.security import generate_password_hash, check_password_hash
from workflowmanager import app #mongo

@app.route("/")
def hello():
    return "I hate this project!"

@app.route("/get_tasks")
def get_tasks():
    tasks = list(mongo.db.tasks.find())
    return render_template("tasks.html", tasks=tasks)