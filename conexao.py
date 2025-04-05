import mysql.connector

chave_conexao = {
    "host": "", # Con banco
    "port": "3306",
    "user": "root",
    "password": "",
}

bd = mysql.connector.connect(**chave_conexao)
cursor = bd.cursor()

cursor.close()
bd.close()

# Conexão com o banco mysql basico