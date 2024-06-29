
class Equipo:
# Constructor
    def __init__(self, id, codigo, nombre, grupo):
        
        # Atributos
        self.id = id
        self.codigo = codigo
        self.nombre = nombre
        self.grupo = grupo
        
    def show(self):
        return(f'''
ID: {self.id}
----------------------------
Equipo: {self.nombre}
Grupo: {self.grupo}
Codigo FIFA: {self.codigo}
____________________________''')