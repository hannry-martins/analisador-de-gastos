import mysql.connector

def conectar():

    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  
        database="analisador"
    )

    return conexao