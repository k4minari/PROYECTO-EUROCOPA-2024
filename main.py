from GestionEquipos import GestionEquipos
import requests

data_equipo = requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/teams.json").json()
data_estadio = requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/stadiums.json").json()
data_partido = requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/matches.json").json()

def main():
    gestion_equipos = GestionEquipos(data_equipo, data_estadio, data_partido)
    gestion_equipos.menu()

main()