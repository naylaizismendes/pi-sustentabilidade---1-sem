import mysql.connector

chave_conexao = {
    "host": "localhost", # Con banco
    "port": "3306",
    "user": "root",
    "password": "",
}
# print(chave_conexao)

def conectar():
    bd = mysql.connector.connect(**chave_conexao)

# Conexão com o banco mysql basico