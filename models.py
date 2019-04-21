# models.py

from flask_login import UserMixin
from . import db


class AreaModel(db.Model):
    __tablename__ = 'area'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    area = db.Column(db.String(60), unique=True, nullable=False)


class PuestoModel(db.Model):
    __tablename__ = 'puesto'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_area = db.Column(db.Integer, db.ForeignKey(
        AreaModel.id), nullable=False)
    descripcion = db.Column(db.String(200), nullable=True)


class RoleModel(db.Model):
    __tablename__ = 'role'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    role = db.Column(db.Integer, unique=True)


class UsuarioModel(UserMixin, db.Model):
    __tablename__ = 'usuario'
    # primary keys are required by SQLAlchemy
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    id_area = db.Column(db.Integer, db.ForeignKey(
        AreaModel.id), nullable=False)
    id_puesto = db.Column(db.Integer, db.ForeignKey(
        PuestoModel.id), nullable=False)
    id_role = db.Column(db.Integer, db.ForeignKey(
        RoleModel.id), nullable=False)


class PublicacionModel(db.Model):
    __tablename__ = 'publicacion'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_user = db.Column(db.String(120), db.ForeignKey(
        UsuarioModel.id), nullable=False)
    asunto = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(200), nullable=True)
    documento = db.Column(db.String(200), nullable=False)
    