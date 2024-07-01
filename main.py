from App import App
import requests

data_equipo = requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/teams.json").json()
data_estadio = requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/stadiums.json").json()
data_partido = requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/matches.json").json()

data_equipo_string = ""
data_estadio_string = ""
data_partido_string = ""

for c in data_equipo:
    data_equipo_string += f'''id: {c["id"]}
code: {c["code"]}
name: {c["name"]}
group: {c["group"]}\n\n'''

with open("Equipo.txt", "w") as equipo:
    equipo.write(data_equipo_string)
    
for c in data_estadio:
    data_estadio_string += f'''id: {c["id"]}
name: {c["name"]}
city: {c["city"]}
capacity: {c["capacity"]}
restaurants: {c["restaurants"]}\n\n'''

with open("Estadio.txt", "w") as estadio:
    estadio.write(data_estadio_string)
    
for c in data_partido:
    data_partido_string += f'''id: {c["id"]}
number: {c["number"]}
home: {c["home"]}
away: {c["away"]}
date: {c["date"]}
group: {c["group"]}
stadium_id: {c["stadium_id"]}\n\n'''

with open("Partido.txt", "w") as partido:
    partido.write(data_partido_string)




def main():
    app = App(data_equipo, data_estadio, data_partido)
    app.menu()
    

main()