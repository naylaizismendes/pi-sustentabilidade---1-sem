import mysql.connector

conexao = mysql.connector(
    host= 'localhost', # Con banco
    user='root',
    port='3306',
    password= "saopaulo",
    database='projeto_sustentabilidade'
)
# print(conexao)
def conectar():
    try:
        bd = mysql.connector.connect(**conexao)
        print("Conexão estabelecida com sucesso!")
        return bd
    except mysql.connector.Error as erro:
        print(f"Erro ao conectar ao MySQL: {erro}")
        return None

# Conexão com o banco mysql basico