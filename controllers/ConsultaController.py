from flask import request, redirect, url_for, Blueprint
from datetime import datetime

#importacion de modelos
from models.Consulta import Consulta
from models.Medico import Medico
from models.Paciente import Paciente

from views import ConsultaView

consulta_bp = Blueprint('consulta', __name__,url_prefix="/consultas")

@consulta_bp.route("/")
def index():
    #Recupera todos los registro de consultas
    consultas = Consulta.get_all()
    return ConsultaView.list(consultas)

@consulta_bp.route("/create", methods=['GET','POST'])
def create():
    if request.method == 'POST':
        fecha_str = request.form['fecha']
        diagnostico = request.form['diagnostico']
        tratamiento = request.form['tratamiento']
        id_medico = request.form['id_medico']
        id_paciente = request.form['id_paciente']
        
        fecha = datetime.strptime(fecha_str, '%Y-%m-%d').date() #Conversion de fecha

        consulta = Consulta(fecha, diagnostico, tratamiento, id_medico, id_paciente )
        consulta.save()
        return redirect(url_for('consulta.index'))
    
    medicos = Medico.query.all()
    pacientes = Paciente.query.all()

    return ConsultaView.create(medicos, pacientes)

@consulta_bp.route("/edit/<int:id_consulta>", methods=['GET','POST'])
def edit(id_consulta):
    consulta = Consulta.get_by_id(id_consulta)
    if request.method == 'POST':
        fecha_str = request.form['fecha']
        diagnostico = request.form['diagnostico']
        tratamiento = request.form['tratamiento']
        id_medico = request.form['id_medico']
        id_paciente = request.form['id_paciente']
        
        fecha = datetime.strptime(fecha_str, '%Y-%m-%d').date() #Conversion de fecha
 
        #actualizar
        consulta.update(fecha=fecha,diagnostico=diagnostico, tratamiento=tratamiento, id_medico=id_medico, id_paciente=id_paciente)
        return redirect(url_for('consulta.index'))

    medicos = Medico.query.all()
    pacientes = Paciente.query.all()
    
    return ConsultaView.edit(consulta, medicos, pacientes)

@consulta_bp.route("/delete/<int:id_consulta>")
def delete(id_consulta):
    consulta = consulta.get_by_id(id_consulta)
    consulta.delete()
    return redirect(url_for('consulta.index'))
