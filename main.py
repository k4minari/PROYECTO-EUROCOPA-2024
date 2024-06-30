from App import App
import requests

data_equipo = requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/teams.json").json()
data_estadio = requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/stadiums.json").json()
data_partido = requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/matches.json").json()
data_cliente = []

def main():
    gestion_equipos = App(data_equipo, data_estadio, data_partido, data_cliente)
    gestion_equipos.menu()

main()