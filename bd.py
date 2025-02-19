import sqlite3

con = sqlite3.connect("atleti.db")
cur = con.cursor()

cur.execute("DROP TABLE IF EXISTS jugadores")
cur.execute("CREATE TABLE jugadores (numero INTEGER PRIMARY KEY, nombre TEXT, edad INTEGER, posicion TEXT, goles INTEGER, asistencias INTEGER, partidos_jugados INTEGER, foto TEXT)")
cur.execute("INSERT INTO jugadores (numero, nombre, edad, posicion, goles, asistencias, partidos_jugados, foto) VALUES (19, 'Julian Álvarez', 25, 'Delantero', 17, 4, 37, 'https://fotografias.larazon.es/clipping/cmsimages01/2025/02/08/B1AD21FF-F4FD-4D67-8695-B085A1817069/98.jpg')")
cur.execute("INSERT INTO jugadores (numero, nombre, edad, posicion, goles, asistencias, partidos_jugados, foto) VALUES (22, 'Giuliano Simeone', 22, 'Delantero', 4, 5, 29, 'https://assets.laliga.com/squad/2024/t175/p482652/2048x2048/p482652_t175_2024_1_002_000.jpg')")
cur.execute("INSERT INTO jugadores (numero, nombre, edad, posicion, goles, asistencias, partidos_jugados, foto) VALUES (5, 'Rodrigo De Paul', 30, 'Centrocampista', 3, 7, 34, 'https://assets.laliga.com/squad/2024/t175/p119141/1024x1024/p119141_t175_2024_1_003_000.png')")

cur.execute("DROP TABLE IF EXISTS partidos")
cur.execute("CREATE TABLE partidos (id INTEGER PRIMARY KEY AUTOINCREMENT, fecha DATE, rival TEXT, ganado BOOLEAN, goles_a_favor INTEGER, goles_en_contra INTEGER, competicion TEXT)")
cur.execute("INSERT INTO partidos (fecha, rival, ganado, goles_a_favor, goles_en_contra, competicion) VALUES ('2022-05-01', 'Real Madrid', 1, 2, 1, 'Liga')")
cur.execute("INSERT INTO partidos (fecha, rival, ganado, goles_a_favor, goles_en_contra, competicion) VALUES ('2022-04-08', 'Barcelona', 0, 1, 3, 'Liga')")
cur.execute("INSERT INTO partidos (fecha, rival, ganado, goles_a_favor, goles_en_contra, competicion) VALUES ('2022-01-15', 'Sevilla', 1, 4, 1, 'Liga')")

cur.execute("DROP TABLE IF EXISTS keys")
cur.execute("CREATE TABLE keys (key TEXT PRIMARY KEY)")
cur.execute("INSERT INTO keys (key) VALUES ('TestKey123')")
cur.execute("INSERT INTO keys (key) VALUES ('Alex')")

# Pruebas
#print(cur.execute("SELECT * FROM jugadores WHERE numero = 19;").fetchall())
con.commit()
con.close()