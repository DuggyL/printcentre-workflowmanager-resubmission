from flask import (
    Flask, flash, render_template, redirect, request, session, url_for)
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from workflowmanager import app, mongo


@app.route("/")
@app.route("/get_tasks")
def get_tasks():
    '''Display tasks'''
    tasks = list(mongo.db.tasks.find())
    return render_template("tasks.html", tasks=tasks)


@app.route("/add_task", methods=["GET", "POST"])
def add_task():
    '''Add task functionality'''
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
    customers = mongo.db.customers.find().sort("company_name", 1)
    return render_template("add_task.html", customers=customers)


@app.route("/edit_task/<task_id>", methods=["GET", "POST"])
def edit_task(task_id):
    '''Edit task functionality'''
    if request.method == "POST":
        is_urgent = "on" if request.form.get("urgent") else "off"
        submit = {
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
        mongo.db.tasks.replace_one({"_id": ObjectId(task_id)}, submit)
        flash("Task Successfully Updated", category='success')
        return redirect(url_for("get_tasks"))
    task = mongo.db.tasks.find_one({"_id": ObjectId(task_id)})
    return render_template("edit_task.html", task=task)


@app.route("/delete_task/<task_id>")
def delete_task(task_id):
    '''Delete task functionality'''
    mongo.db.tasks.delete_one({"_id": ObjectId(task_id)})
    flash("Task Successfully Deleted", category='success')
    return redirect(url_for("get_tasks"))


@app.route("/register", methods=["GET", "POST"])
def register():
    '''Register account functionality'''
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists", category='error')
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!", category='success')
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    '''Login account functionality'''
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome, {}".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password", category='error')
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password", category='error')
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    '''Display user's profile page'''
    # find session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    '''Remove user from user's session cookie'''
    flash("You have been logged out", category='success')
    # remove user's session cookies
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/get_customers")
def get_customers():
    '''Display customers list'''
    # find company's information from db
    customers = list(mongo.db.customers.find().sort("company_name", 1))
    return render_template("customers.html", customers=customers)


@app.route("/add_customer", methods=["GET", "POST"])
def add_customer():
    '''Add customer functionality'''
    if request.method == "POST":
        customer = {
            "company_name": request.form.get("company_name"),
            "customer_name": request.form.get("customer_name"),
            "contact_no": request.form.get("contact_no"),
            "email": request.form.get("email"),
            "address": request.form.get("address"),
        }
        mongo.db.customers.insert_one(customer)
        flash("Customer Successfully added", category='success')
        return redirect(url_for("get_customers"))
    return render_template("add_customer.html")


@app.route("/edit_customer/<customer_id>", methods=["GET", "POST"])
def edit_customer(customer_id):
    '''Edit customer functionality'''
    if request.method == "POST":
        submit = {
            "company_name": request.form.get("company_name"),
            "customer_name": request.form.get("customer_name"),
            "contact_no": request.form.get("contact_no"),
            "email": request.form.get("email"),
            "address": request.form.get("address")
        }
        mongo.db.customers.replace_one({"_id": ObjectId(customer_id)}, submit)
        flash("Customer Successfully Updated", category='success')
        return redirect(url_for("get_customers"))
    customers = mongo.db.customers.find().sort("company_name", 1)
    return render_template("edit_customer.html", customers=customers)


@app.route("/delete_customer/<customer_id>")
def delete_customer(customer_id):
    '''Delete customer functionality'''
    mongo.db.customers.delete_one({"_id": ObjectId(customer_id)})
    flash("Customer Successfully Deleted", category='success')
    return redirect(url_for("get_customers"))


@app.route("/search", methods=["GET", "POST"])
def search():
    '''Search functionality'''
    query = request.form.get("query")
    customers = list(mongo.db.customers.find({"$text": {"$search": query}}))
    return render_template("customers.html", customers=customers)
