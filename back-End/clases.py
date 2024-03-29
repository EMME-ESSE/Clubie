from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *
from flask_wtf.file import FileField, FileAllowed, FileSize
from rutas import *
from datetime import datetime


app.config['SECRET_KEY'] = 'clave_secreta'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database2.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    cedula = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    telefono = db.Column(db.Integer, nullable=False, unique=True)
    email = db.Column(db.String(30), nullable=False, unique=True)
    

class RegistrationForm(FlaskForm):
    name = StringField('name', validators=[validators.Length(min=6, max=25)])
    cedula = IntegerField('cedula', validators=[validators.NumberRange(min=1000000, max=99999999)])
    telefono = IntegerField('telefono', validators=[validators.NumberRange(min=10000000, max=999999999)])
    email = StringField('email', validators=[validators.Length(min=6, max=35)])

class EditForm(FlaskForm):
    cedula = StringField('cedula', validators=[DataRequired()])
    name = StringField('name', validators=[DataRequired()])
    telefono = StringField('telefono', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    submit = SubmitField('Guardar cambios')

class Club(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    campoarchivo = db.Column(db.String(30))
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(70))

class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(
        min=6, max=6)], render_kw={"placeholder": "Usuario"})
    password = PasswordField(validators=[InputRequired(), Length(
        min=6, max=6)], render_kw={"placeholder": "Contraseña"})
    submit = SubmitField("Iniciar")

class Trazabilidad(db.Model):
    idplanta = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    raza = db.Column(db.String(30), nullable=False, unique=True)
    Enraizado = db.Column(db.DateTime, nullable=True)
    Riego = db.Column(db.DateTime, nullable=True)
    paso1 = db.Column(db.DateTime, nullable=True)
    paso2 = db.Column(db.DateTime, nullable=True)
    paso3 = db.Column(db.DateTime, nullable=True)
    floracion = db.Column(db.DateTime, nullable=True)
    cosecha = db.Column(db.DateTime, nullable=True)
    cantidad = db.Column(db.String(3), nullable=False)
    observaciones = db.Column(db.String(80), nullable=True)

class PlantForm(FlaskForm):
    idplanta = IntegerField('idplanta')
    raza = StringField('raza')    
    Enraizado = DateTimeLocalField('Enraizado', format='%Y-%m-%dT%H:%M', validators=[Optional()])
    Riego = DateTimeLocalField('Riego', format='%Y-%m-%dT%H:%M', validators=[Optional()])
    paso1 = DateTimeLocalField('paso1', format='%Y-%m-%dT%H:%M', validators=[Optional()])
    paso2 = DateTimeLocalField('paso2', format='%Y-%m-%dT%H:%M', validators=[Optional()])
    paso3 = DateTimeLocalField('paso3', format='%Y-%m-%dT%H:%M', validators=[Optional()])
    floracion = DateTimeLocalField('floracion', format='%Y-%m-%dT%H:%M', validators=[Optional()])
    cosecha = DateTimeLocalField('cosecha', format='%Y-%m-%dT%H:%M', validators=[Optional()])

    cantidad = StringField('cantidad')
    observaciones = StringField('observaciones')

class Ventasform(FlaskForm):
    cedulaVenta = SelectField('cedulaVenta')
    razaVenta = StringField('razaVenta')
    cantVenta = IntegerField('cantVenta')
    retiro = DateTimeLocalField('retiro', format='%Y-%m-%dT%H:%M')

class Ventas(db.Model):
    idventas = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    cedula = db.Column(db.String(20), nullable=False)
    raza = db.Column(db.String(30), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    retiro = db.Column(db.DateTime, default=datetime.now())