# Python API Test

### Python API test created to practice concepts learned in class

---

> [!NOTE]  
> Currently, the API supports the following two endpoints:

```
/jugadores/<PlayerNumber><PlayerName>
```

```
/ultimospartidos/<n>
```

> Recent matches are ordered from most recent to oldest, with 0 being the latest match played.

<br><br>

For example:

```
/jugador/Julian%20Álvarez
```

```
/jugador/22
```

```
/ultimospartidos/2
```

<br><br>

> [!IMPORTANT]  
> Before running `api.py`, remember to run `bd.py` to create the database (If it doesnt already exist).

<br>

> [!CAUTION]  
> To run the code, you need to have the following dependencies installed:

- sqlite3  
- flask

