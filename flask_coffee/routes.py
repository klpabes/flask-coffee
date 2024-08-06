from flask import render_template, url_for, flash, redirect
from flask_coffee import app
# from app.forms import RegistrationForm, LoginForm

@app.route("/")
def index():
    return render_template('index.html')

