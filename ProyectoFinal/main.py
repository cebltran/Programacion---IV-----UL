from flask import  Flask, render_template, request, redirect, url_for, flash
from celery import Celery
import config

import Ficha
import BD
from bson.raw_bson import RawBSONDocument
import bsonjs
tipo=3

app = Flask(__name__)
app.secret_key = 'mysecretkey'
client = Celery(app.name)

@app.route('/creabd', methods = ['GET'])
def creabase():
    BD.CreaBD()
    return 'Base creada Con exito'

# CARGA INICIAL
@app.route('/', methods = ['GET'])
def Index():
    base = BD
    consulta = base.BuscaDato("",2)
    return render_template('index.html', contacs=consulta)


@app.route('/correo/<string:id> <string:NOMBRE> <string:FECHA> <string:HORA> <string:CORREO>')
def correo(id, NOMBRE, FECHA, HORA, CORREO):

    significado = 'Respetado(a), ' + NOMBRE + ' le notificamos que su cita ha sido '
    if tipo == 1:
        significado = significado + 'Cancelada: '
    if tipo == 2:
        significado = significado + 'Modificada: '

    if tipo == 3:
        significado = significado + 'Agendada: '

    significado = significado + 'Fecha: ' + FECHA
    significado = significado + 'Hora: ' +  HORA

    config.eviocorreo(CORREO, significado)
    flash('Correo Enviado Satisfactoriamente ' + significado)
    return redirect(url_for('Index'))


# EDITAR
@app.route('/edit/<string:id>')
def editar(id):
        base = BD
        salida = base.BuscaDato(id, 3)
        for dato in salida:
                return render_template('edit.html',contacts = dato)
#Actualizar
@app.route('/update/<string:id>', methods = ['POST'])
def update(id):
        base = BD
        if request.method == 'POST':
                documento = request.form['DOCUMENTO']
                nombre = request.form['NOMBRE']
                correo = request.form['CORREO']
                telefono = request.form['TELEFONO']
                fecha = request.form['FECHA']
                hora = request.form['HORA']
                base.Editadato (documento, nombre, correo, telefono, fecha, hora, id)
                flash('Dato Actualizado Satisfactoriamente')
                return redirect(url_for('Index'))
#Agregar
@app.route('/agregar', methods = ['POST'])
def agregar():
        base = BD
        if request.method == 'POST':
                documento = request.form['DOCUMENTO']
                nombre = request.form['NOMBRE']
                correo = request.form['CORREO']
                telefono = request.form['TELEFONO']
                fecha = request.form['FECHA']
                hora = request.form['HORA']
                base.Insertadato(documento, nombre, correo, telefono, fecha, hora)
                flash('Dato Agregado Satisfactoriamente')
                return redirect(url_for('Index'))
#Brrar
@app.route('/delete/<string:id>')
def delete(id):
        base = BD
        base.Borradato(id)
        flash('Dato Borrado Satisfactoriamente')
        return redirect(url_for('Index'))


@app.route('/ficha/<string:dato>', methods = ['GET'])
def getfichapordato(dato):
        for reg in fichas:

            if str(reg["dato"]) == str(dato):

                retorno = reg
                return jsonify(retorno), 200
            else:
                retorno = "-1"

        if retorno == "-1":
            return "No hay datos"


if __name__== "__main__":
    app.run(debug = True)

