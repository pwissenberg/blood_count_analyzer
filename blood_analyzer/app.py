"""Main file which initalizes the app."""
from flask import Flask, render_template

from data import models

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("home.html")


@app.route("/manual-input")
def manual_input():


    return render_template("manualinput.html")


app.run()
