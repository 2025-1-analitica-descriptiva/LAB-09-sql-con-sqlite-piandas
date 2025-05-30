import sqlite3
import pandas as pd

# 1. Conecta (o crea) la base:
conn = sqlite3.connect("files/input/mydb.sqlite")

# 2. Para cada CSV, lee con pandas y vuelca a SQLite:
for nombre in ("tbl0", "tbl1", "tbl2"):
    filepath = f"files/input/{nombre}.csv"
    if nombre == "tbl0":
        # tbl0: K0 CHAR(1), c01 INT, c02 INT, c03 CHAR(4), c04 FLOAT
        df = pd.read_csv(
            filepath,
            header=None,
            names=["K0", "c01", "c02", "c03", "c04"]
        )
    elif nombre == "tbl1":
        # tbl1: K0 CHAR(1), K1 INT, c12 FLOAT, c13 INT, c14 DATE, c15 FLOAT, c16 CHAR(4)
        df = pd.read_csv(
            filepath,
            header=None,
            names=["K0", "K1", "c12", "c13", "c14", "c15", "c16"]
        )
    else:  # nombre == "tbl2"
        # tbl2: K1 INT, c21 FLOAT, c22 INT, c23 DATE, c24 FLOAT, c25 CHAR(5)
        df = pd.read_csv(
            filepath,
            header=None,
            names=["K1", "c21", "c22", "c23", "c24", "c25"]
        )
    df.to_sql(nombre, conn, if_exists="replace", index=False)


# 3. Cierra conexión:
conn.close()
