from flask import Flask, render_template, url_for, flash, redirect, jsonify
from SGDA import app, db, bcrypt, role
from SGDA.forms import RegistrationForm, LoginForm
from flask_bcrypt import Bcrypt
from flask_user import login_required



@app.route("/")
@app.route("/home")
def home():
    classrooms = db.aulas
    return render_template('home.html', classrooms=classrooms, role=role)


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        email = form.email.data
        username = form.username.data
        password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        db.users.insert_one({ "email":email, "username":username, "password":password, "profile":"student"})  
     
        return redirect(url_for('login'))
    return render_template('register.html', form=form, role=role)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    username = form.email.data
    global role
    if (username == "admin" or username == "student" or username == "secretary"):
        role = username
        return render_template('home.html', role=username)
    return render_template('login.html', form=form, role = role )

@app.route("/classRoomReserve", methods=['GET', 'POST'])
def classRoomReserve():
    form = LoginForm()
    global role
    classrooms = db.aulas.find()
    return render_template('classRoomReserve.html', classrooms=classrooms, role=role)

@app.route("/modifyProfile", methods=['GET', 'POST'])
def modifyProfile():
    form = LoginForm()
    return render_template('modifyProfile.html')

@app.route("/members", methods=['GET', 'POST'])
def members():
    form = LoginForm()
    return render_template('login.html', form=form)


@app.route("/classrom/reserve/historial", methods=['GET', 'POST'])
def mereserveHistorialmbers():
    form = LoginForm()
    return render_template('reserveHistorial.html', form=form)

@app.route("/cargarAulas", methods=['GET', 'POST'])
def cargarAulas():
    form = LoginForm()
    return render_template('cargarAulas.html', form=form,role=role)


@app.route("/recoverPassword", methods=['GET', 'POST'])
def recoverPassword():
    form = LoginForm()
    return render_template('recoverPassword.html', form=form)

@app.route("/logout", methods=['GET', 'POST'])
def logout():
    form = LoginForm()
    global role
    role = "none"
    return redirect(url_for('home'))

@app.route("/indicators", methods=['GET', 'POST'])
def indicators():
    form = LoginForm()
    return render_template('indicators.html', form=form, role=role)

@app.route("/userprofile", methods=['GET', 'POST'])
def userprofile():
    form = LoginForm()
    return render_template('userprofile.html', form=form, role=role)

@app.route("/userRequests", methods=['GET', 'POST'])
def userRequests():
    form = LoginForm()
    return render_template('userRequests.html', form=form, role=role)

@app.route("/reserveHistorial", methods=['GET', 'POST'])
def reserveHistorial():
    form = LoginForm()
    return render_template('reserveHistorial.html', form=form, role=role)

@app.route("/modifyAula", methods=['GET', 'POST'])
def modifyAula():
    form = LoginForm()
    return render_template('modifyAula.html', form=form, role=role)
