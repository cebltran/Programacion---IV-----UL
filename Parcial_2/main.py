from flask import Flask, jsonify, request
import Ficha

app = Flask(__name__)
fichas = Ficha.fichas


@app.route('/ficha', methods = ['GET'])
def getficha():
        return jsonify(fichas),200

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

