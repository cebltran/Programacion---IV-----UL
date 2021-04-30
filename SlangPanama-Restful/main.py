from flask import  Flask, render_template, request, redirect, url_for, flash, Response, jsonify
from celery import Celery
import json
from bson.json_util import dumps
from bson import json_util


#https://www.youtube.com/watch?v=GsCCyN3fRoI

import DB
import config

app = Flask(__name__)
app.secret_key = 'mysecretkey'
client = Celery(app.name)


@app.route('/')
def Index():
        base = DB
        salida = base.BuscaDato("",2)
        #return salida
        #return salida
        #return jsonify({"message":"Carga Realizada con exito"})
        return render_template('index.html', contacs = salida)
        #return jsonify({"salida" : salida})

@app.route('/creabd')
def creabd():
        return 'Slang Panameño'

# parcialmodulo8@gmail.com
@app.route('/correo/<string:id>')
def correo(id):
        return render_template('correo.html',contacts = 1)


@app.route('/enviar/<string:id>', methods = ['POST'])

def enviar(id):
        if request.method == 'POST':
                palabra = request.form['correo']
                significado = request.form['texto']
                config.eviocorreo(palabra, significado)
                flash('Correo Enviado Satisfactoriamente')
                return redirect(url_for('Index'))

#enviar.apply_async((2, 2), link=add.s(16))

@app.route('/edit/<string:id>')
def editar(id):
        base = DB
        salida = base.BuscaDato(id, 3)
        for dato in salida:
                return render_template('edit.html',contacts = dato)



@app.route('/update/<string:id>', methods = ['POST'])
def update(id):
        base = DB
        if request.method == 'POST':
                palabra = request.form['expresion']
                significado = request.form['significado']
                base.Editadato (palabra, significado,  id)
                flash('Dato Actualizado Satisfactoriamente')
                return redirect(url_for('Index'))


@app.route('/agregar', methods = ['POST'])
def agregar():
        base = DB
        if request.method == 'POST':
                # palabra = request.form['expresion']
                # significado = request.form['significado']
                palabra = request.form['expresion']
                significado = request.form['significado']
                base.Insertadato(palabra.upper(), significado.upper())
                flash('Dato Agregado Satisfactoriamente')
                return redirect(url_for('Index'))


@app.route('/delete/<string:id>')
def delete(id):
        base = DB
        base.Borradato(id)
        flash('Dato Borrado Satisfactoriamente')
        return redirect(url_for('Index'))


@app.route('/buscar')
def buscar():
        return 'Slang Panameño'
if __name__ == '__main__':
    app.run(debug = True)

