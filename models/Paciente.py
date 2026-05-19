from database import db

class Paciente(db.Model):
    __tablename__ = 'pacientes'

    id_paciente = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(255), nullable = False)
    edad = db.Column(db.Integer, nullable = False)
    direccion = db.Column(db.String(20), nullable = False)
    telefono = db.Column(db.String(200), nullable = False)

    #Relacion con consulta 1:N
    consultas = db.relationship('Consulta', back_populates='paciente')


    #Metodo constructor
    def __init__ (self, nombre, edad, direccion, telefono):
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion
        self.telefono = telefono

    #Guardar datos
    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Paciente.query.all()

    def get_by_id(id_paciente):
        return Paciente.query.get(id_paciente)

    def update(self, nombre=None, edad=None, direccion=None, telefono=None):
        if nombre and edad and direccion and telefono:
            self.nombre = nombre
            self.edad = edad
            self.direccion = direccion
            self.telefono = telefono
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()