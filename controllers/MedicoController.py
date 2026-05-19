from flask import request, redirect, url_for, Blueprint
from models.Medico import Medico
from views import MedicoView

medico_bp = Blueprint('medico', __name__,url_prefix="/medicos")

@medico_bp.route("/")
def index():
    #Recupera todos los registro de medicos
    medicos = Medico.get_all()
    return MedicoView.list(medicos)

@medico_bp.route("/create", methods=['GET','POST'])
def create():
    if request.method == 'POST':
        nombre = request.form['nombre']
        especialidad = request.form['especialidad']
        telefono = request.form['telefono']
        email = request.form['email']
        

        medico = Medico(nombre, especialidad, telefono, email )
        medico.save()
        return redirect(url_for('medico.index'))
    
    return MedicoView.create()

@medico_bp.route("/edit/<int:id_medico>", methods=['GET','POST'])
def edit(id_medico):
    medico = Medico.get_by_id(id_medico)
    if request.method == 'POST':
        nombre = request.form['nombre']
        especialidad = request.form['especialidad']
        telefono = request.form['telefono']
        email = request.form['email']
        
 
        #actualizar
        medico.update(nombre=nombre,especialidad=especialidad, telefono=telefono, email=email)
        return redirect(url_for('medico.index'))

    return MedicoView.edit(medico)

@medico_bp.route("/delete/<int:id_medico>")
def delete(id_medico):
    medico = Medico.get_by_id(id_medico)
    medico.delete()
    return redirect(url_for('medico.index'))
