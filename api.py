from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route('/jugador/<jugadorAConsultar>')
def jugador(jugadorAConsultar):
    if esNumero(jugadorAConsultar):
        jugador = consultar(f"SELECT * FROM jugadores WHERE numero = {int(jugadorAConsultar)};")
    else :
        jugador = consultar(f"SELECT * FROM jugadores WHERE nombre = '{jugadorAConsultar}';")

    return {"numero": jugador[0], "nombre": jugador[1], "edad": jugador[2], "posicion": jugador[3], "goles": jugador[4], "asistencias": jugador[5], "partidos_jugados": jugador[6]}

@app.route('/ultimospartidos/<n>')
def partido(n):
    partido = consultar(f"SELECT * FROM partidos ORDER BY fecha DESC LIMIT 1 OFFSET {n};")
    return {"id": partido[0], "fecha": partido[1], "rival": partido[2], "ganado": partido[3], "goles_a_favor": partido[4], "goles_en_contra": partido[5], "competicion": partido[6]}

def consultar(consulta):
    con = sqlite3.connect("atleti.db")
    cur = con.cursor()
    cur.execute(consulta)
    resultado = cur.fetchone()
    con.close()
    return resultado

def esNumero(n):
    try:
        int(n)
        return True
    except ValueError:
        return False

if __name__ == '__main__':
    app.run()