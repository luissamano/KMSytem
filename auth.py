# auth.py

from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from .models import UsuarioModel
from . import db

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/login', methods=['POST'])
@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = UsuarioModel.query.filter_by(email=email).first()

    # check if user actually exists
    # take the user supplied password, hash it, and compare it to the hashed password in database
    if not user or not check_password_hash(user.password, password):
        flash('Por favor, compruebe sus datos de inicio de sesión y vuelva a intentarlo.')
        # if user doesn't exist or password is wrong, reload the page
        return redirect(url_for('auth.login'))

    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)
    return redirect(url_for('main.profile'))


@auth.route('/signup')
def signup():
    return render_template('signup.html')


@auth.route('/signup', methods=['POST'])
def signup_post():

    email = request.form.get('email')
    name = request.form.get('nombre')
    password = request.form.get('password')
    role = request.form.get('role')
    area = request.form.get('area')
    puesto = request.form.get('puesto')

    # Si el usuario ya existe muestra el error.
    user = UsuarioModel.query.filter_by(email=email).first()

    if user:
        flash('La dirección de correo ya existe.')
        return redirect(url_for('auth.signup'))

    # Crea un nuevo objecto listo para insertar.
    new_user = UsuarioModel(email=email,
                            password=generate_password_hash(
                                password, method='sha256'),
                            name=name,
                            id_area=area, id_puesto=puesto, id_role=role)

    # Agrega el nuevo usuario a la base de datos.
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
