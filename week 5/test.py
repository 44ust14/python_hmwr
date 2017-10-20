# -*- coding:utf-8 -*-
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        return redirect(url_for("hello", name = name, email = email))



    return render_template("home.html")
@app.route("/hello", methods=["GET"])
def hello():
    val1 = request.args["name"]
    val2 = request.args["email"]
    context = {
        "name": val1,
        "email": val2
    }


    return render_template("hello.html", context=context)

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        name = request.form.get('name', '')
        email = request.form.get('email', '')
        return render_template("hello.html")


@app.route("/logout")
def logout():
    return render_template("logout.html")




if __name__ == '__main__':
    app.run(debug=True,port=8001)
