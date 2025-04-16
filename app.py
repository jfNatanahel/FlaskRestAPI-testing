from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Crear la aplicación Flask
app = Flask(__name__)

# Configuración de la base de datos (reemplaza los valores con tus datos)
#app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.getenv('control_fzyp_user')}:{os.getenv('ECCmPYrvMteFm6D6kmomXq8OTwbYOtx6')}@{os.getenv('dpg-cvoosbqdbo4c73b72pk0-a.oregon-postgres.render.com')}:{os.getenv('5432')}/{os.getenv('control_fzyp')}"
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Desactivar las modificaciones de seguimiento para evitar advertencias

# Inicializar SQLAlchemy
db = SQLAlchemy(app)

# Definir los modelos que representan las tablas de tu base de datos

class Cliente(db.Model):
    __tablename__ = 'clientes'  # El nombre de la tabla
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    telefono = db.Column(db.String(50))
    tipo_plan = db.Column(db.String(50))
    fecha_inicio = db.Column(db.Date)

    # Relación con la tabla pagos
    pagos = db.relationship('Pago', backref='cliente', lazy=True)
    asistencias = db.relationship('Asistencia', backref='cliente', lazy=True)

class Pago(db.Model):
    __tablename__ = 'pagos'
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'), nullable=False)
    monto = db.Column(db.Numeric(10, 2))
    fecha_pago = db.Column(db.Date)
    metodo_pago = db.Column(db.String(50))

class Asistencia(db.Model):
    __tablename__ = 'asistencias'
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'), nullable=False)
    fecha_asistencia = db.Column(db.Date)

class Empleado(db.Model):
    __tablename__ = 'empleados'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    rol = db.Column(db.String(50))
    usuario = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

# Ruta para obtener todos los clientes
@app.route('/clientes', methods=['GET'])
def get_clientes():
    clientes = Cliente.query.all()  # Obtener todos los registros de clientes

    # Convertir los resultados a formato JSON
    clientes_list = []
    for cliente in clientes:
        clientes_list.append({
            'id': cliente.id,
            'nombre': cliente.nombre,
            'telefono': cliente.telefono,
            'tipo_plan': cliente.tipo_plan,
            'fecha_inicio': cliente.fecha_inicio.strftime('%Y-%m-%d')
        })
    
    return jsonify(clientes_list)

# Ruta para obtener todos los pagos de un cliente
@app.route('/pagos/<int:cliente_id>', methods=['GET'])
def get_pagos(cliente_id):
    pagos = Pago.query.filter_by(cliente_id=cliente_id).all()  # Filtrar pagos por cliente_id

    # Convertir los resultados a formato JSON
    pagos_list = []
    for pago in pagos:
        pagos_list.append({
            'id': pago.id,
            'monto': str(pago.monto),  # Convertir a string para evitar problemas con JSON
            'fecha_pago': pago.fecha_pago.strftime('%Y-%m-%d'),
            'metodo_pago': pago.metodo_pago
        })
    
    return jsonify(pagos_list)

# Ruta para obtener todas las asistencias de un cliente
@app.route('/asistencias/<int:cliente_id>', methods=['GET'])
def get_asistencias(cliente_id):
    asistencias = Asistencia.query.filter_by(cliente_id=cliente_id).all()  # Filtrar asistencias por cliente_id

    # Convertir los resultados a formato JSON
    asistencias_list = []
    for asistencia in asistencias:
        asistencias_list.append({
            'id': asistencia.id,
            'fecha_asistencia': asistencia.fecha_asistencia.strftime('%Y-%m-%d')
        })
    
    return jsonify(asistencias_list)

if __name__ == '__main__':
    app.run(debug=True)
