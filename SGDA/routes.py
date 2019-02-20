from flask import Flask, render_template, url_for, flash, redirect, jsonify, request, session
from SGDA import app, db, bcrypt, User, login_manager, role
from SGDA.forms import RegistrationForm
from flask_user import login_required
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt


@app.route("/")
@app.route("/home")
def home():
    classrooms = db.aulas.find()
    if 'email' in session:
        usuarios = db.usuarios
        login_user = usuarios.find_one({'email': session['email']})
        return render_template('home.html', classrooms=classrooms, role=session['email'],usr_data = login_user)
    return render_template('home.html', classrooms=classrooms, role='none')

@app.route("/register", methods=['GET', 'POST'])
def register():
    if 'email' in session:
        return redirect(url_for('home'))
    else:
        form = RegistrationForm()
        if request.method == 'POST':
            usuarios = db.usuarios
            existing_user = usuarios.find_one({'email' : form.email.data})
            if existing_user is None:
                hashpass = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
                usuarios.insert_one({'_id':usuarios.count()+1,'email': form.email.data, 'password': hashpass, 'username':form.username.data})
                session['email'] = form.email.data
                return redirect(url_for('home'))
            return 'Usuario ya registrado'
        return render_template('register.html',form = form, role = 'none')
    

@app.route('/login', methods=['GET','POST'])
def login():
    if 'email' in session:
        return redirect(url_for('home'))
    else:
        form = RegistrationForm()
        if request.method == 'POST':
            usuarios = db.usuarios
            login_user = usuarios.find_one({'email': form.email.data})
            if login_user:
                if  bcrypt.check_password_hash(login_user['password'],form.password.data):
                    session['email'] = form.email.data
                    return redirect(url_for('home'))
            return render_template('login.html', form=form, role = 'none',error=True) 
    return render_template('login.html', form=form, role = 'none',error=False) 
     
@app.route("/classRoomReserve", methods=['GET', 'POST'])
def classRoomReserve():
    form = RegistrationForm()
    classrooms = db.aulas.find()
    usuarios = db.usuarios
    login_user = usuarios.find_one({'email': session['email']})
    #Código para el manejo de la reserva.. conexión con mongo, crear documento, etc...
 
    if 'email' in session:
        return render_template('classRoomReserve.html', classrooms=classrooms, role = session['email'], usr_data=login_user)
    return render_template('classRoomReserve.html', classrooms=classrooms, role = 'none')

@app.route("/modifyProfile", methods=['GET', 'POST'])
def modifyProfile():
    if 'email' in session:
        usuarios = db.usuarios
        login_user = usuarios.find_one({'email': session['email']})
        form = RegistrationForm()
        #comentario par git
        if request.method == 'POST':
            usuarios.update_one(
                {'_id':login_user['_id']},
                {'$set':{"nombre":form.nombre.data,"apellido":form.apellido.data,"email":form.email.data,"telefono":form.telefono.data,"direccion":form.direccion.data}},
                upsert=True
            )
            redirect(url_for('modifyProfile'))
        else:
            return render_template('modifyProfile.html', role = session['email'], usr_data = login_user, usuarios = usuarios, form = form)
    return redirect(url_for('home'))
    
@app.route("/cargarAulas", methods=['GET', 'POST'])
def cargarAulas():
    if 'email' in session and session['email'] == 'jefedpto@ciens.ucv.ve':
        usuarios = db.usuarios
        login_user = usuarios.find_one({'email': session['email']})
        form = RegistrationForm()
        return render_template('cargarAulas.html', form=form, role = session['email'], usr_data=login_user)
    return redirect(url_for('home'))

@app.route("/recoverPassword", methods=['GET', 'POST'])
def recoverPassword():
    form = RegistrationForm()
    if 'email' in session:
        return redirect(url_for('home'))
    return render_template('recoverPassword.html', form=form, role = 'none')

@app.route("/logout", methods=['GET', 'POST'])
def logout():
    if 'email' in session:
        session.pop('email')
    return redirect(url_for('home'))

@app.route("/indicators", methods=['GET', 'POST'])
def indicators():
    if 'email' in session and ( session['email'] == 'secretaria@ciens.ucv.ve' or session['email'] == 'jefedpto@ciens.ucv.ve' ):
        usuarios = db.usuarios
        login_user = usuarios.find_one({'email': session['email']})
        form = RegistrationForm()
        return render_template('indicators.html', form=form, role = session['email'],usr_data = login_user)
    return redirect(url_for('home'))

@app.route("/userprofile", methods=['GET', 'POST'])
def userprofile():
    form = RegistrationForm()   
    if 'email' in session:
        usuarios = db.usuarios
        login_user = usuarios.find_one({'email': session['email']})
        return render_template('userprofile.html', form=form, role = session['email'],usr_data=login_user)
    return redirect(url_for('home'))

@app.route("/userRequests", methods=['GET', 'POST'])
def userRequests():
    if 'email' in session and ( session['email'] == 'secretaria@ciens.ucv.ve' or session['email'] == 'jefedpto@ciens.ucv.ve' ):
        usuarios = db.usuarios
        login_user = usuarios.find_one({'email': session['email']})
        form = RegistrationForm()
        return render_template('userRequests.html', form=form, role = session['email'],usr_data=login_user)
    return redirect(url_for('home'))

@app.route("/reserveHistorial", methods=['GET', 'POST'])
def reserveHistorial():
    if 'email' in session:
        usuarios = db.usuarios
        login_user = usuarios.find_one({'email': session['email']})
        form = RegistrationForm()
        return render_template('reserveHistorial.html', form=form, role = session['email'],usr_data=login_user)
    return redirect(url_for('home'))

@app.route("/listaUsuarios", methods=['GET', 'POST'])
def listaUsuarios():
    if 'email' in session and ( session['email'] == 'secretaria@ciens.ucv.ve' or session['email'] == 'jefedpto@ciens.ucv.ve' ):
        usuarios = db.usuarios
        form = RegistrationForm()
        return render_template('listaUsuarios.html', form=form, role = session['email'],usuarios=usuarios)
    return redirect(url_for('home'))


@app.route("/modifyAula", methods=['GET', 'POST'])
def modifyAula():
    if 'email' in session and ( session['email'] == 'secretaria@ciens.ucv.ve' or session['email'] == 'jefedpto@ciens.ucv.ve' ):
        usuarios = db.usuarios
        login_user = usuarios.find_one({'email': session['email']})
        form = RegistrationForm()
        return render_template('modifyAula.html', form=form, role = session['email'],usr_data=login_user)
    return redirect(url_for('home'))
