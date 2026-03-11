import pandas as pd
from database import conectar

def analisar():

    con = conectar()

    query = "SELECT * FROM gastos"

    df = pd.read_sql(query, con)

    total = df["valor"].sum()
    media = df["valor"].mean()
    maior = df["valor"].max()

    categorias = df.groupby("categoria")["valor"].sum()

    return total, media, maior, categorias.to_dict()