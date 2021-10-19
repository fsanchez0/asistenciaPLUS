from flask import Flask, request, render_template, redirect, url_for, flash
from waitress import serve
from flask_sqlalchemy import SQLAlchemy
import os

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "mssql+pymssql://sapp:Pemex.2020*@vwtutsqlp065.un.pemex.com/PEMEX"

app = Flask(__name__)
app.secret_key = 'mysecretkey'
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Asistencias(db.Model): #Clase Asistencias = Tabla Asistencias
    __tablename__ = 'Asistencias'

    ID = db.Column(db.Integer, nullable=False, primary_key=True)
    NOMBRE = db.Column(db.String(60))
    EDAD = db.Column(db.Integer)
    TELEFONO = db.Column(db.String(15))
    TELEFONO_MOVIL = db.Column(db.String(15))
    CORREO = db.Column(db.String(255))
    FORMACION_ACADEMICA = db.Column(db.String(255))
    CATEGORIA_PROPUESTOS = db.Column(db.String(30))
    ORIGEN = db.Column(db.String(255))
    F_PROGRAMACION = db.Column(db.DATETIME)
    RESPONSABLE = db.Column(db.String(255))
    HORARIO_ESCALONADO = db.Column(db.String(25))
    ID_BT = db.Column(db.Integer)
    TIPO_LICENCIA = db.Column(db.String(255))
    OBS = db.Column(db.String(255))
    PRUEBA_MANEJO = db.Column(db.String(10))
    APTO = db.Column(db.String(10))
    MMPI = db.Column(db.String(10))
    RESULTADO_MMPI = db.Column(db.String(255))
    CAPACITACION_SEGURIDAD = db.Column(db.String(10))
    DOCUMENTACION = db.Column(db.String(10))

    def __repr__(self):
        return "<Nombre: {}>".format(self.NOMBRE)

    def to_dict(self):
        return {
            'id': self.ID,
            'nombre': self.NOMBRE,
            'edad': self.EDAD,
            'telefono': self.TELEFONO,
            'telefono_movil': self.TELEFONO_MOVIL,
            'correo': self.CORREO,
            'formacion_academica': self.FORMACION_ACADEMICA,
            'categoria_propuestos': self.CATEGORIA_PROPUESTOS,
            'origen': self.ORIGEN,
            'f_programacion': self.F_PROGRAMACION,
            'responsable': self.RESPONSABLE,
            'horario_escalonado': self.HORARIO_ESCALONADO,
            'id_bt': self.ID_BT,
            'tipo_licencia': self.TIPO_LICENCIA,
            'obs': self.OBS,
            'prueba_manejo': self.PRUEBA_MANEJO,
            'apto': self.APTO,
            'mmpi': self.MMPI,
            'resultado_mmpi': self.RESULTADO_MMPI,
            'capacitacion_seguridad': self.CAPACITACION_SEGURIDAD,
            'documentacion': self.DOCUMENTACION
        }


@app.route('/', methods=["GET", "POST"])
def home():
    return render_template("home.html", title='Inicio')


@app.route('/api/data')
def data():
    query = Asistencias.query
    return {
        'data': [asistencia.to_dict() for asistencia in query]
    }


@app.route('/addReg')
def addRegister():
    return render_template('addReg.html', title='Nuevo Registro')


@app.route('/addReg', methods=['POST'])
def add_register():
    if request.method == 'POST':
        if request.form:
            try:
                asistencia = Asistencias()
                asistencia.NOMBRE = request.form['NOMBRE']
                asistencia.EDAD = int(request.form['EDAD'])
                asistencia.TELEFONO = request.form['TELEFONO']
                asistencia.TELEFONO_MOVIL = request.form['TELEFONO_MOVIL']
                asistencia.CORREO = request.form['CORREO']
                asistencia.FORMACION_ACADEMICA = request.form['FORMACION_ACADEMICA']
                asistencia.CATEGORIA_PROPUESTOS = request.form['CATEGORIA_PROPUESTOS']
                asistencia.ORIGEN = request.form['ORIGEN']
                asistencia.F_PROGRAMACION = request.form['F_PROGRAMACION']
                asistencia.RESPONSABLE = request.form['RESPONSABLE']
                asistencia.HORARIO_ESCALONADO = request.form['HORARIO_ESCALONADO']
                asistencia.ID_BT = int(request.form['ID_BT'])
                asistencia.TIPO_LICENCIA = request.form['TIPO_LICENCIA']
                asistencia.OBS = request.form['OBS']
                asistencia.PRUEBA_MANEJO = request.form['PRUEBA_MANEJO']
                asistencia.APTO = request.form['APTO']
                asistencia.MMPI = request.form['MMPI']
                asistencia.RESULTADO_MMPI = request.form['RESULTADO_MMPI']
                asistencia.CAPACITACION_SEGURIDAD = request.form['CAPACITACION_SEGURIDAD']
                asistencia.DOCUMENTACION = request.form['DOCUMENTACION']
                db.session.add(asistencia)
                db.session.commit()
                flash('Usuario agregado exitosamente')
            except Exception as e:
                flash('Falló al agregar: ', e)
                print(e)
        return redirect(url_for('home'))


@app.route('/editReg/<id>')
def get_register(id):
    asistencia = Asistencias.query.filter_by(ID=id).first()
    return render_template('editReg.html', reg=asistencia, title='Editar Registro')


@app.route('/updateReg/<id>', methods=['POST'])
def updateReg(id):
    print("Voy a actualizar: ", Asistencias.query.filter_by(ID=id).first())
    if request.method == 'POST':
        try:
            asistencia = Asistencias.query.filter_by(ID=id).first()
            if asistencia is not None:
                asistencia.NOMBRE = request.form['NOMBRE']
                asistencia.EDAD = int(request.form['EDAD'])
                asistencia.TELEFONO = request.form['TELEFONO']
                asistencia.TELEFONO_MOVIL = request.form['TELEFONO_MOVIL']
                asistencia.CORREO = request.form['CORREO']
                asistencia.FORMACION_ACADEMICA = request.form['FORMACION_ACADEMICA']
                asistencia.CATEGORIA_PROPUESTOS = request.form['CATEGORIA_PROPUESTOS']
                asistencia.ORIGEN = request.form['ORIGEN']
                asistencia.F_PROGRAMACION = request.form['F_PROGRAMACION']
                asistencia.RESPONSABLE = request.form['RESPONSABLE']
                asistencia.HORARIO_ESCALONADO = request.form['HORARIO_ESCALONADO']
                asistencia.ID_BT = int(request.form['ID_BT'])
                asistencia.TIPO_LICENCIA = request.form['TIPO_LICENCIA']
                asistencia.OBS = request.form['OBS']
                asistencia.PRUEBA_MANEJO = request.form['PRUEBA_MANEJO']
                asistencia.APTO = request.form['APTO']
                asistencia.MMPI = request.form['MMPI']
                asistencia.RESULTADO_MMPI = request.form['RESULTADO_MMPI']
                asistencia.CAPACITACION_SEGURIDAD = request.form['CAPACITACION_SEGURIDAD']
                asistencia.DOCUMENTACION = request.form['DOCUMENTACION']
                db.session.commit()
                flash('Actualizado con éxito')
        except Exception as e:
            flash('Falló al actualizar: ', e)
            print(e)
    return redirect(url_for('home'))


@app.route('/deleteReg/<id>')
def delete_register(id):
    flash('Usuario borrado exitosamente')
    asistencia = Asistencias.query.filter_by(ID=id).first()
    db.session.delete(asistencia)
    db.session.commit()
    return redirect(url_for('home'))


#if __name__ == '__main__':
 #   app.run()
serve(app, host='0.0.0.0', port=8080, threads=1)
