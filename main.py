# main.py
from flask import Blueprint, render_template
from flask_login import login_required, current_user
from sqlalchemy import create_engine
import json
engine = create_engine('sqlite:///db.sqlite', echo = True)

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user)

from .models import PublicacionModel
from . import db

@main.route('/publicaciones')
@login_required
def publicaciones():
        items = []
        conn = engine.connect()
        post =  db.select([PublicacionModel])
        result = conn.execute(post)
        print(result)
        for row in result:
                items.append({'id': row[0], 'id_user': row[1], 'asunto': row[2], 'descripcion': row[3], 'documento': row[4]})
        
        conn.close()
        return render_template('publicaciones.html', result=items )


@main.route('/newpost')
@login_required
def newpost():
    return render_template('newpost.html', user=current_user)



@main.route('/nuevodata')
@login_required
def nuevodata():
    return render_template('puesto_area.html')