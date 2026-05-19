from database import db

class Medico(db.Model):
    __tablename__ = 'medicos'

    id_consulta = db.Column(db.Integer, primary_key = True)
    fecha = db.Column(db.String(255), nullable = False)
    diagnostico = db.Column(db.String(100), nullable = False)
    tratamiento = db.Column(db.String(20), nullable = False)
    id_medico = db.Column(db.Integer, db.ForeignKey('medicos.id_medico'), nullable = False)
    id_paciente = db.Column(db.Integer, db.ForeignKey('pacientes.id_paciente'), nullable = False)

    #Relaciones
    medico = db.relationship('Medico', back_populates='consultas')
    paciente = db.relationship('Paciente', back_populates='consultas')


    #Metodo constructor
    def __init__ (self, fecha, diagnostico, tratamiento, id_medico):
        self.fecha = fecha
        self.diagnostico = diagnostico
        self.tratamiento = tratamiento
        self.id_medico = id_medico

    #Guardar datos
    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Medico.query.all()

    def get_by_id(id_medico):
        return Medico.query.get(id_medico)

    def update(self, nombre=None, especialidad=None, telefono=None, correo=None):
        if nombre and especialidad and telefono and correo:
            self.nombre = nombre
            self.especialidad = especialidad
            self.telefono = telefono
            self.correo = correo
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()