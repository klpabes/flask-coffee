from flask import render_template, url_for, flash, redirect
from flask_coffee import app, db, bcrypt
from flask_coffee.forms import RegistrationForm, LoginForm
from flask_coffee.models import User, Product

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
    return render_template('about.html', title='About')

@app.route("/blog")
def blog():
    return render_template('blog.html', title='Blog')

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@coffee.com' and form.password.data == 'password':
            flash('You are now logged in!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Login Unsuccessful, please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)