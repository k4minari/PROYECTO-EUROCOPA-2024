import requests

equipos = requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/teams.json").json()

info_equipos = ""

class Equipo:
# Constructor
    def __init__(self, id, codigo, nombre, grupo):
        
        # Atributos
        self.id = id
        self.codigo = codigo
        self.nombre = nombre
        self.grupo = grupo
        
    def show(self):
        print(f'''
ID: {self.id}
----------------------------
Equipo: {self.nombre}
Grupo: {self.grupo}
Codigo FIFA: {self.codigo}
____________________________''')