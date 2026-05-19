from flask import Flask, request

#Importacion de controladores
from controllers import MedicoController
# from controllers import PacientesController
# from controllers import ConsultasController 

from database import db

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///clinica.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

app.register_blueprint(MedicoController.medico_bp)


@app.context_processor
def inject_active_path():
    def is_active(path):
        return 'active' if request.path == path else ''
    return (dict(is_active=is_active))

@app.route('/')
def home():
    return "<h1> Sistema de Gestión de Clínica Médica </h1>"


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)


