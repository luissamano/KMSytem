# main.py

from flask import Blueprint, render_template
from flask_login import login_required, current_user

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)


@main.route('/publicaciones')
@login_required
def publicaciones():
    return render_template('publicaciones.html', name=current_user.name)


@main.route('/sendemail')
def email():
    return render_template(
        'email.html',
        name=current_user.name,
        tipo_usuario=current_user.id_role)
