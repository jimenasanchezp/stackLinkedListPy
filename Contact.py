class Contact:
    def __init__(self, id, nombre, telefono):
        self.id = id # id del contacto
        self.nombre = nombre # nombre del contacto
        self.telefono = telefono # teléfono del contacto

    def __eq__(self, other):
        if isinstance(other, Contact): 
            return self.id == other.id # dos contactos son iguales si tienen el mismo id
        return False # si 'other' no es contacto, devuelve falso

    def __str__(self):
        return f"ID:{self.id}, Nombre:{self.nombre}, Tel:{self.telefono}"
