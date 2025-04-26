import mysql.connector

# con banco
def obtemConexao (servidor, usuario, senha, bd):
   if obtemConexao.conexao==None:
       obtemConexao.conexao = mysql.connector.connect(f"host={servidor};"
                                                      f"user={usuario};"
                                                      f"password={senha};"
                                                      f"database={bd};")
   return obtemConexao.conexao
obtemConexao.conexao=None

# insert 
def insercao_de_aluno (ra,nome):
    comando=f"insert into Alunos (RA,Nome) values ({ra},'{nome}’)" 
    conexao=obtemConexao("172.16.12.14","XXXXX","YYYYY","XXXXX")
    cursor=conexao.cursor()
    cursor.execute(comando)
    cursor.commit()

# select
def selecao_de_aluno (ra):
    comando=f"select * from Alunos where RA={ra}" 
    conexao=obtemConexao("172.16.12.14","XXXXX","YYYYY","XXXXX")
    cursor=conexao.cursor()
    cursor.execute(comando)
    linhas=cursor.fetchall()
    if linhas==[]: return None
    return linhas[0]

# select all
def selecao_de_alunos ( ):
    comando=("select * from Alunos")
    conexao=obtemConexao("172.16.12.14","XXXXX","YYYYY","XXXXX")
    cursor=conexao.cursor()
    cursor.execute(comando)
    linhas=cursor.fetchall()
    return linhas

def fechaConexao ( ):
    conexao=obtemConexao("172.16.12.14","XXXXX","YYYYY","XXXXX")
    cursor.close()
    conexão.close()

    
