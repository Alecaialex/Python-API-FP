import sqlite3

con = sqlite3.connect("atleti.db")
cur = con.cursor()

cur.execute("DROP TABLE IF EXISTS jugadores")
cur.execute("CREATE TABLE jugadores (numero INTEGER PRIMARY KEY, nombre TEXT, edad INTEGER, posicion TEXT, goles INTEGER, asistencias INTEGER, partidos_jugados INTEGER)")
cur.execute("INSERT INTO jugadores (numero, nombre, edad, posicion, goles, asistencias, partidos_jugados) VALUES (19, 'Julian Álvarez', 25, 'Delantero', 17, 4, 37)").fetchone()
cur.execute("INSERT INTO jugadores (numero, nombre, edad, posicion, goles, asistencias, partidos_jugados) VALUES (22, 'Giuliano Simeone', 22, 'Delantero', 4, 5, 29)").fetchone()
cur.execute("INSERT INTO jugadores (numero, nombre, edad, posicion, goles, asistencias, partidos_jugados) VALUES (5, 'Rodrigo De Paul', 30, 'Centrocampista', 3, 7, 34)").fetchone()
cur.execute("DROP TABLE IF EXISTS partidos")
cur.execute("CREATE TABLE partidos (id INTEGER PRIMARY KEY AUTOINCREMENT, fecha DATE, rival VARCHAR(30), ganado BOOLEAN, goles_a_favor INTEGER, goles_en_contra INTEGER, competicion TEXT)")
cur.execute("INSERT INTO partidos (fecha, rival, ganado, goles_a_favor, goles_en_contra, competicion) VALUES ('2022-05-01', 'Real Madrid', 1, 2, 1, 'Liga')").fetchone()
cur.execute("INSERT INTO partidos (fecha, rival, ganado, goles_a_favor, goles_en_contra, competicion) VALUES ('2022-04-08', 'Barcelona', 0, 1, 3, 'Liga')").fetchone()
cur.execute("INSERT INTO partidos (fecha, rival, ganado, goles_a_favor, goles_en_contra, competicion) VALUES ('2022-01-15', 'Sevilla', 1, 4, 1, 'Liga')").fetchone()

# Pruebas
#print(cur.execute("SELECT * FROM jugadores WHERE numero = 19;").fetchall())
con.commit()
con.close()