from flask import Flask, render_template, url_for, flash, redirect, jsonify
from SGDA import app, db, bcrypt
from SGDA.forms import RegistrationForm, LoginForm
from flask_bcrypt import Bcrypt
from flask_user import login_required, UserManager, UserMixin

@app.route("/")
@app.route("/home")
def home():
    classrooms = db.aulas.find()
    return render_template('home.html', classrooms=classrooms)


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        email = form.email.data
        username = form.username.data
        password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        db.users.insert_one({ "email":email, "username":username, "password":password, "profile":"student"})  
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', form=form)

@app.route("/members", methods=['GET', 'POST'])
def members():
    form = LoginForm()
    return render_template('login.html', form=form)