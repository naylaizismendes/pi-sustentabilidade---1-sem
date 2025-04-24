import mysql.connector
def conectar():
    try:
        conexao = mysql.connector.connect(
            host= 'localhost', # Con banco
            user='root',
            port='3306',
            password= "saopaulo",
            database='projeto_sustentabilidade'
)
        if conexao.is_connected():
            print('conectadoo com sucesso')
            return conexao
    except mysql.connector.Error as erro:
        print("Erro ao conectar ao MySQL:", erro)
        return None



# Conexão com o banco mysql basico