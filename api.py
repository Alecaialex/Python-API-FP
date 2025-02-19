from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/jugador/<jugadorAConsultar>')
def jugador(jugadorAConsultar):
    key = request.args.get('key')
    if validarKey(key) == False:
        return "Key inválida", 401
    if esNumero(jugadorAConsultar):
        jugador = consultar(f"SELECT * FROM jugadores WHERE numero = {int(jugadorAConsultar)};")
    else :
        jugador = consultar(f"SELECT * FROM jugadores WHERE nombre = '{jugadorAConsultar}';")

    return {"numero": jugador[0], "nombre": jugador[1], "edad": jugador[2], "posicion": jugador[3], "goles": jugador[4], "asistencias": jugador[5], "partidos_jugados": jugador[6], "imagen": jugador[7]}

@app.route('/ultimospartidos/<n>')
def partido(n):
    key = request.args.get('key')
    if validarKey(key) == False:
        return "Key inválida", 401
    partido = consultar(f"SELECT * FROM partidos ORDER BY fecha DESC LIMIT 1 OFFSET {n};")
    return {"id": partido[0], "fecha": partido[1], "rival": partido[2], "ganado": partido[3], "goles_a_favor": partido[4], "goles_en_contra": partido[5], "competicion": partido[6], "imagen": jugador[7]}

@app.errorhandler(404)
def page_not_found(error):
    return "Recurso no encontrado", 404

def validarKey(key):
    if "'" in key or "=" in key or ";" in key or "--" in key:
        return False
    return consultar(f"SELECT * FROM keys WHERE key = '{key}';") != None

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
    app.run(host='0.0.0.0')