from flask import Flask

#Importacion de controladores
# from controllers import MedicoController
# from controllers import PacientesController
# from controllers import ConsultasController 

from database import db

app = Flask(__name__)


@app.route('/')
def home():
    return "<h1> Aplicacion de Citas Medicas </h1>"


if __name__ == '__main__':
    app.run(debug=True)


