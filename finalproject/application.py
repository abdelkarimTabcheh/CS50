import os
import requests
import datetime

from cs50 import SQL
from flask_session import Session
from tempfile import mkdtemp
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from functools import wraps

from flask import redirect, render_template, request, session
from functools import wraps

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///list.db")

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    if request.method == "POST":
        show = request.form.get("show")
        date = request.form.get("date")

        if "include" in request.form:
            task = {'task' : '', 'id' : '', 'date' : date, 'type' : 'Register'}
            return render_template("task.html", task=task)

        if "up" in request.form:
            orders = db.execute("SELECT orders FROM tasks WHERE id = ? ", int(request.form['up'][4:]))

            if orders[0]["orders"] > 1:
                db.execute("UPDATE tasks SET orders = orders + 1 WHERE orders = ? AND date = ? AND user_id = ?", orders[0]["orders"]-1, date, session["user_id"])
                db.execute("UPDATE tasks SET orders = orders - 1 WHERE id = ? ", int(request.form['up'][4:]))

        if "down" in request.form:
            orders = db.execute("SELECT orders FROM tasks WHERE id = ? ", int(request.form['down'][5:]))
            larger = db.execute("SELECT MAX(orders) orders FROM tasks WHERE user_id = ? AND date = ?", session["user_id"], date)

            if orders[0]["orders"] != maior[0]["orders"]:
                db.execute("UPDATE tasks SET orders = orders - 1 WHERE orders = ? AND date = ? AND user_id = ?", orders[0]["orders"]+1, date, session["user_id"])
                db.execute("UPDATE tasks SET orders = orders + 1 WHERE id = ? ", int(request.form['down'][5:]))

        if "done" in request.form:
            db.execute("UPDATE tasks set done = 'S' WHERE id = ? ", int(request.form['done'][5:]))

        if "undone" in request.form:
            db.execute("UPDATE tasks set done = 'N' WHERE id = ? ", int(request.form['undone'][8:]))

        if "change" in request.form:
            task = db.execute("SELECT task, id, date, 'Change' type FROM tasks WHERE id = ?", int(request.form['change'][6:]))
            return render_template("task.html", task=task[0])

        if "exclude" in request.form:
            orders = db.execute("SELECT orders FROM tasks WHERE id = ?", int(request.form['exclude'][6:]))

            db.execute("UPDATE tasks SET orders = orders - 1 WHERE date = ? AND user_id = ? AND orders > ?", date, session["user_id"], orders[0]["orders"])
            db.execute("DELETE FROM tasks WHERE id = ? ", int(request.form['exclude'][6:]))

        if "seg" in request.form:
            dates = datetime.datetime.strptime(date, "%Y-%m-%d")
            date = (dates + datetime.timedelta(days=1)).strftime('%Y-%m-%d')


        if "ant" in request.form:
            dates = datetime.datetime.strptime(date, "%Y-%m-%d")
            date = (dates - datetime.timedelta(days=1)).strftime('%Y-%m-%d')

        if "Hide" in request.form:
            if request.form.get("show") == 'S':
                show = 'N'
            else:
                show = 'S'

        if show == 'N':
            todo = db.execute("SELECT id, task, done FROM tasks WHERE user_id = ? AND date = ? AND done = 'N' GROUP BY orders", session["user_id"], date)
        else:
            todo = db.execute("SELECT id, task, done FROM tasks WHERE user_id = ? AND date = ? GROUP BY orders", session["user_id"], date)

        return render_template("todo.html", todo=todo, date=date, show=show)

    else:
        date = f"{datetime.datetime.now():%Y-%m-%d}"
        todo = db.execute("SELECT id, task, done FROM tasks WHERE user_id = ? AND date = ? GROUP BY orders", session["user_id"], date)

        return render_template("todo.html", todo=todo, date=date, show='S')

@app.route("/task", methods=["GET", "POST"])
@login_required
def task():
    if request.method == "POST":
        orders = 1
        row = db.execute("SELECT MAX(orders) orders FROM tasks WHERE user_id = ? AND date = ?", session["user_id"], request.form.get("date"))
        if row[0]["orders"] != None:
            orders = row[0]["orders"] + 1

        if request.form['change'][6:] != "":
            date = db.execute("SELECT date, orders FROM tasks WHERE id = ?", int(request.form['change'][6:]))

            if date[0]["date"] != request.form.get("date"):
                db.execute("UPDATE tasks SET task = ?, date = ?, orders = ? WHERE id = ? ", request.form.get("task"), request.form.get("date"), orders, int(request.form['change'][6:]))

                db.execute("UPDATE tasks SET orders = orders - 1 WHERE date = ? AND user_id = ? AND orders > ?", data[0]["date"], session["user_id"], data[0]["orders"])
            else:
                db.execute("UPDATE tasks SET task = ?, date = ? WHERE id = ? ", request.form.get("task"), request.form.get("date"), int(request.form['change'][6:]))

        else:
            db.execute("INSERT INTO tasks (task, date, user_id, orders) VALUES(?, ?, ?, ?)",
                       request.form.get("task"), request.form.get("date"), session["user_id"], orders)

        todo = db.execute("SELECT id, task, done FROM tasks WHERE user_id = ? AND date = ? GROUP BY orders", session["user_id"], request.form.get("date"))

        return render_template("todo.html", todo=todo, date=request.form.get("date"), show='S')

    else:
        return render_template("task.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    session.clear()

    if request.method == "POST":
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))
        erro = ''

        if len(rows) != 1 or not check_password_hash(rows[0]["password"], request.form.get("password")):
            erro = 'Check login and password to continue.'
            return render_template("login.html", erro=erro)

        session["user_id"] = rows[0]["id"]

        return redirect("/")
    else:
        return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        retorna_erro = 'N'
        erro = ''

        if request.form.get("password") != request.form.get("confirmation"):
            erro = 'Different password.'
            retorna_erro = 'S'

        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        if len(rows) == 1:
            erro = 'login'
            retorna_erro = 'S'

        if retorna_erro == 'S':
            return render_template("register.html", erro=erro)

        name = request.form.get("name")
        username = request.form.get("username")
        password = generate_password_hash(request.form.get("password"))

        user_id = db.execute("INSERT INTO users (name, username, password) VALUES(?, ?, ?)", name, username, password)

        session["user_id"] = user_id

        return redirect("/")
    else:
        return render_template("register.html")

@app.route("/logout")
def logout():
    session.clear()

    return redirect("/")
