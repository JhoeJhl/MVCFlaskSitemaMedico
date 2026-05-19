from flask import request, redirect, url_for, Blueprint
from models.Paciente import Paciente
from views import PacienteView

paciente_bp = Blueprint('paciente', __name__,url_prefix="/pacientes")

@paciente_bp.route("/")
def index():
    #Recupera todos los registro de pacientes
    pacientes = Paciente.get_all()
    return PacienteView.list(pacientes)

@paciente_bp.route("/create", methods=['GET','POST'])
def create():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = request.form['edad']
        direccion = request.form['direccion']
        telefono = request.form['telefono']
        

        paciente = Paciente(nombre, edad, direccion, telefono )
        paciente.save()
        return redirect(url_for('paciente.index'))
    
    return PacienteView.create()

@paciente_bp.route("/edit/<int:id_paciente>", methods=['GET','POST'])
def edit(id_paciente):
    paciente = Paciente.get_by_id(id_paciente)
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = request.form['edad']
        direccion = request.form['direccion']
        telefono = request.form['telefono']
        
 
        #actualizar
        paciente.update(nombre=nombre,edad=edad, direccion=direccion, telefono=telefono)
        return redirect(url_for('paciente.index'))

    return PacienteView.edit(paciente)

@paciente_bp.route("/delete/<int:id_paciente>")
def delete(id_paciente):
    paciente = Paciente.get_by_id(id_paciente)
    paciente.delete()
    return redirect(url_for('paciente.index'))
