# Python API Test

### Python API test created to practice concepts learned in class

---

> [!NOTE]  
> Currently, the API supports the following two endpoints:

```
/players/<Number><Name>
```

```
/recentmatches/<n>
```

> Recent matches are ordered from most recent to oldest, with 0 being the latest match played.

<br><br>

For example:

```
/players/Julian%20Álvarez
```

```
/players/22
```

```
/recentmatches/2
```

<br><br>

> [!IMPORTANT]  
> Before running `api.py`, remember to run `bd.py` to create the database.

<br>

> [!CAUTION]  
> To run the code, you need to have the following dependencies installed:

- sqlite3  
- flask

