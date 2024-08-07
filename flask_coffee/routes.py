from flask import render_template, url_for, flash, redirect
from flask_coffee import app
# from app.forms import RegistrationForm, LoginForm

index_items = [
    {
        'name': 'Latte',
        'desc': 'Popular coffee drink made with espresso and steamed milk.',
        'price': 150,
        'date_posted': 'August 6, 2024'
    },
    {
        'name': 'Capuccino',
        'desc': 'A classic coffee beverage made with equal parts espresso, steamed milk, and milk foam.',
        'price': 175,
        'date_posted': 'August 6, 2024'
    },
    {
        'name': 'Americano',
        'desc': 'A classic coffee drink by diluting a shot of espresso with hot water.',
        'price': 100,
        'date_posted': 'August 6, 2024'
    },
]


@app.route("/")
def index():
    return render_template('index.html', index_items=index_items)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/blog")
def blog():
    return render_template('blog.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/register")
def register():
    return render_template('register.html')