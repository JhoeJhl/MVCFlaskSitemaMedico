from database import db

class Medico(db.Model):
    __tablename__ = 'medicos'

    id_medico = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(255), nullable = False)
    especialidad = db.Column(db.String(100), nullable = False)
    telefono = db.Column(db.String(20), nullable = False)
    correo = db.Column(db.String(200), nullable = False)

    #Relacion con consultas
    consultas = db.relationship('Consulta', back_populates='medico')

    #Metodo constructor
    def __init__ (self, nombre, especialidad, telefono, correo):
        self.nombre = nombre
        self.especialidad = especialidad
        self.telefono = telefono
        self.correo = correo

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