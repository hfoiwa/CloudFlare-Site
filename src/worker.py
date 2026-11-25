from flask import Flask, request, Response, Blueprint, make_response, render_template, url_for, redirect
from workers import wsgi
from flask_login import LoginManager, AnonymousUserMixin, login_required
from pyodide import ffi

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "/login"


@app.get("/")
def index():
    page_data = {
        
    }
    return render_template("index.html", **page_data)

@app.get("/game/sudoku")
def sudoku_menu():
    page_data = {

    }
    return render_template("sudoku_menu.html", **page_data)


@app.get("/game/sudoku/<mode>", defaults={"seed": ""})
@app.get("/game/sudoku/<mode>/<seed>")
def sudoku_ingame(mode="", seed=""):
    page_data = {
        "mode" : mode,
        "seed" : seed
    }
    return render_template("sudoku_ingame.html", **page_data)


@app.get("/profile")
@login_required
def profile():

    return render_template("profile.html")

@app.get("/register")
def register():

    return render_template("register.html")

@app.route("/login", methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        # Check credentials sent in form data

        return redirect(url_for("index"))

    else:

        return render_template("login.html")

@app.get("/logout")
def logout():

    return redirect(url_for("index"))


@login_manager.user_loader
def user_loader(userid: str):
    return None

Default = wsgi.entrypoint(app)