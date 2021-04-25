from flask import  Flask, render_template, request, redirect, url_for, flash
import DB


app = Flask(__name__)
app.secret_key = 'mysecretkey'


@app.route('/')
def Index():
        base = DB
        salida = base.BuscaDato("",2)
        return render_template('index.html',contacs = salida )

@app.route('/creabd')
def creabd():
        return 'Slang Panameño'

@app.route('/agregar', methods = ['POST'])
def agregar():
        base = DB
        if request.method == 'POST':
                palabra = request.form['expresion']
                significado = request.form['significado']
                base.Insertadato(palabra.upper(), significado.upper())
                flash('Dato Agregado Satisfactoriamente')
                return redirect(url_for('Index'))

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
    app.run(debug=True)

