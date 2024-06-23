from GestionEquipos import GestionEquipos
import requests

data_equipo = requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/teams.json").json()

def main():
    gestion_equipos = GestionEquipos(data_equipo)
    gestion_equipos.menu()

main()