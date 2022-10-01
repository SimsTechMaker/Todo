import imp
from flask import Flask, render_template, url_for, make_response
from .views import app


@app.route("/")
def index():
    return make_response("salut le monde")