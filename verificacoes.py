
import mysql.connector

#ao entrar no programa 
def primeiro_contato ():
   print(" _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
   print("|                                                               |")
   print("|     Sistema de Monitoramento de Sustentabilidade Pessoal      |")        
   print("|_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|")
   print("|                                                               |")
   print("| 1. Inserir dados de monitoramento                             |") # feito
   print("| 2. Alterar dados de monitoramento                             |") #feito
   print("| 3. Apagar dados de monitoramento                              |") #feito
   print("| 4. Listar cada monitoramento diário e classificar             |") #feito
   print("| 5. Calcular e mostrar as médias dos parâmetros e classificar  |") 
   print("| 6. Sair do sistema                                            |") #feito
   print("|_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|")
   print()
   

#conexao  
def obtemConexao (localhost, root, saopaulo, projeto_sustentabilidade):
   if obtemConexao.conexao==None:
      obtemConexao.conexao = mysql.connector.connect(host    =f"{localhost}",\
                                                     user    =f"{root}",\
                                                     password=f"{saopaulo}",\
                                                     database=f"{projeto_sustentabilidade}")

   return obtemConexao.conexao
obtemConexao.conexao=None
   
#inserir no banco       
def insercao_dados (data, qtd_de_agua_litros, uso_energia_eletria_kwh, residuos_nao_reciclaveis_kg, porcentagem_de_reciclado_hoje, transporte_publico, bicicleta, caminhada, carro, carro_eletrico, carona):
   comando = "INSERT INTO verficador" +\
             "(data, qtd_de_agua_litros , uso_energia_eletrica_kwh," +\
             "residuos_nao_reciclaveis_kg , porcentagem_de_reciclado_hoje," +\
             "transporte_publico, bicicleta, caminhada, carro , carro_eletrico , carona) " +\
             "VALUES" +\
            f"('{data}', '{qtd_de_agua_litros}', '{uso_energia_eletria_kwh}', '{residuos_nao_reciclaveis_kg}', '{porcentagem_de_reciclado_hoje}','{transporte_publico}', '{bicicleta}', '{caminhada}', '{carro}', '{carro_eletrico}', '{carona}')"

   conexao=obtemConexao("localhost","root","saopaulo","projeto_sustentabilidade") #arrumar
   cursor=conexao.cursor()
   cursor.execute(comando)
   conexao.commit()

#inserir valores 
from datetime import datetime
def inserir ():
   while True:
      entrada_data = input('Digite a data atual (DDMMYYYY): ')
      try:
         data = datetime.strptime(entrada_data, "%d%m%Y").date()
         break
      except ValueError:
         print("Data inválida. Por favor, insira no formato DDMMYYYY.")

   validador = False
   while not validador:
      try:
         qtd_de_agua_litros=float(input('Quantos litros de água você consumiu hoje: '))
      except ValueError:
         print('Inválido, o valor deve ser numérico; Tente novamente!')
      else:
         validador = True
    
   validador = False
   while not validador:
      try:
         uso_energia_eletrica_kwh=float(input('Quantos kWh de energia elétrica você consumiu hoje: '))
      except ValueError:
         print('Inválido, o valor deve ser numérico; Tente novamente!')
      else:
         validador = True

   validador = False
   while not validador:
      try: 
         residuos_nao_reciclaveis_kg = float(input('Quantos kg de resíduos não recicláveis você gerou hoje: '))
      except ValueError:
         print('Inválido, o valor deve ser numérico; Tente novamente!')
      else: 
         validador = True

   validador = False
   while not validador:
      try:
         porcentagem_de_reciclado_hoje= float(input('Qual e a porcentagem de resíduos reciclados no total em (%): '))
      except ValueError:
         print('Inválido, o valor deve ser numérico; Tente novamente!')
      else:
         validador = True

   print ('Quais meios de transporte você utilizou hoje? Responda apenas (S / N)')

   transportePublico= input('1. Transporte público (Ônibus,metrô, trem): ').upper()
   while transportePublico not in ('S', 'N'):
      print('Resposta inválida. Por favor, digite S ou N.')
      transportePublico = input('1. Transporte público (Ônibus,metrô, trem): ').upper()

   bicicleta = input('2. Bicicleta: ').upper()
   while bicicleta not in ('S', 'N'):
      print('Resposta inválida. Por favor, digite S ou N.')
      bicicleta = input('2. Bicicleta: ').upper()
 
   caminhada = input('3. Caminhada: ').upper()
   while caminhada not in ('S', 'N'):
      print('Resposta inválida. Por favor, digite S ou N.')
      caminhada = input('3. Caminhada: ').upper()

   carro = input('4. Carro (Combustível Fóssil): ').upper()
   while carro not in ('S', 'N'):
      print('Resposta inválida. Por favor, digite S ou N.')
      carro = input('4. Carro (Combustível Fóssil): ').upper()

   carroEletrico= input('5. Carro elétrico: ').upper()
   while carroEletrico not in ('S', 'N'):
      print('Resposta inválida. Por favor, digite S ou N.')
      carroEletrico = input('5. Carro elétrico: ').upper()

   carona= input('6. Carona compartilhada (Fósseis): ').upper()
   while carona not in ('S', 'N'):
      print('Resposta inválida. Por favor, digite S ou N.')
      carona = input('6. Carona compartilhada (Fósseis): ').upper()

   print("\n Dados inseridos com sucesso!\n")

#atualizar uma informação
def alterar ():
    
    data_atualizar = input("Digite a data que deseja alterar (AAAA-MM-DD): ")
    #escolher oq quer mudar
    print(" _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
    print("|                                                    |")
    print("|                Menu de Atualização:                |")  
    print("| _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|")  
    print("|                                                    |")    
    print("| 1 - Atualizar água (L)                             |")              
    print("| 2 - Atualizar energia eletrica (kwh)               |")
    print("| 3 - Atualizar residuos não reciclados (kg)         |")
    print("| 4 - Atualizar reciclados (%)                       |")
    print("| 5 - Atualizar uso de transporte público (S/N)      |")
    print("| 6 - Atualizar uso de caminhada (S/N)               |") 
    print("| 7 - Atualizar uso de bicicleta (S/N)               |")
    print("| 8 - Atualizar uso de carro (S/N)                   |")
    print("| 9 - Atualizar uso de carro elétrico (S/N)          |")
    print("| 10 - Atualizar uso de carona (S/N)                 |")
    print("| _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|")
    
    
    dados = {
        '1': 'qtd_de_agua_litros',
        '2': 'uso_energia_eletrica_kwh',
        '3': 'residuos_nao_reciclaveis_kg',
        '4': 'porcentagem_de_reciclado_hoje',
        '5': 'transporte_publico',
        '6': 'caminhada',
        '7': 'bicicleta',
        '8': 'carro',
        '9': 'carro_eletrico',
        '10':'carona'
    }
    while True:
        dados_opcao = input("Digite o número do campo que deseja atualizar: ")
        if dados_opcao in dados:
            break
        else: 
            print("Opção não existe; Tente novamente!")
    
    novo_valor = input(f"Digite o novo valor para {dados[dados_opcao]}: ")

    comando = f"UPDATE verficador SET {dados} = %s WHERE data = %s"
    conexao=obtemConexao("localhost","root","saopaulo","projeto_sustentabilidade") 
    cursor=conexao.cursor()
    cursor.execute(comando)
    conexao.commit()
    print("Atualização realizada com sucesso!")
   
   
def excluir ():
   confirmacao = input('Tem certeza que deseja excluir o ultimo dado cadastrado? ').upper()
   while confirmacao not in ('S', 'N'):
      print('Resposta inválida. Por favor, digite S ou N.')
      carona = input('Tem certeza que deseja excluir o ultimo dado cadastrado? ').upper()
   
   if confirmacao == 'S':
      data_excluir = input("Digite a data que deseja deletar: ")
      comando = "DELETE FROM verficador WHERE data = %s"
      conexao=obtemConexao("localhost","root","saopaulo","projeto_sustentabilidade")
      cursor=conexao.cursor()
      cursor.execute(comando)
      print("Registro deletado com sucesso!\n")
   else :
      print('Sistema encerrado!')

#lista todos os registros       
def listar ():
   comando=("SELECT * FROM verficador")
   conexao=obtemConexao("localhost","root","saopaulo","projeto_sustentabilidade")
   cursor=conexao.cursor()
   cursor.execute(comando)
   linhas=cursor.fetchall()
   return linhas

def medias (): 
   conexao = obtemConexao("localhost", "root", "saopaulo", "projeto_sustentabilidade")
   cursor = conexao.cursor()

   cursor.execute("""
      SELECT 
         AVG(qtd_de_agua_litros), 
         AVG(uso_energia_eletrica_kwh), 
         AVG(residuos_nao_reciclaveis_kg), 
         AVG(porcentagem_de_reciclado_hoje )
      FROM verficador
      """)
   media = cursor.fetchone()

   print("Média Geral do Sistema:")
   print(f"Água: {media[0]:.2f} L")
   print(f"Energia: {media[1]:.2f} kWh")
   print(f"Resíduos: {media[2]:.2f} kg") #nao tem?
   print(f"Reciclado: {media[3]:.2f} %")

   # água
   if media[0] < 150:
      print('Consumo de Água: Alta sustentabilidade')
   elif media[0] >= 150 and media[0] <= 200:
      print('Consumo de Água: Moderada sustentabilidade')
   else:
      print('Consumo de Água: Baixa sustentabilidade')

   # energia
   if media[1] < 5:
      print('Consumo de Energia Elétrica: Alta sustentabilidade')
   elif media[1] >= 5 and media[1] <= 10:
      print('Consumo de Energia Elétrica: Moderada sustentabilidade')
   else:
      print('Consumo de Energia Elétrica: Baixa sustentabilidade')
      
   # resíduos reciclados 
   if media[3] < 20:
      print('Porcentagem de resíduos reciclados: Baixa sustentabilidade')
   elif media[3] >= 20 and media[3] <= 50:
      print('Porcentagem de resíduos reciclados: Moderada sustentabilidade')
   else:
      print('Porcentagem de resíduos reciclados: Alta sustentabilidade') 

   sustentavel = 0
   naoSustentavel = 0

   if transportePublico == 'S':
      sustentavel += 1
   if bicicleta == 'S':
      sustentavel +=1
   if caminhada == 'S':
      sustentavel += 1
   if carro == 'S':
      naoSustentavel+= 1
   if carroEletrico == 'S':
      sustentavel+= 1
   if carona == 'S':
      naoSustentavel+= 1


   if sustentavel >=1 and naoSustentavel == 0:
      print("Uso de transporte: Alta sustentabilidade")
   elif sustentavel == 0 and naoSustentavel >= 1:
      print("Uso de transporte: Baixa sustentabilidade")
   else:
      print("Uso de transporte: Sustentabilidade moderada")

   cursor.close()
         
def fechaConexao ():
    conexao=obtemConexao("localhost","root","saopaulo","projeto_sustentabilidade")
    cursor=conexao.cursor()
    cursor.close()
    conexao.close()
    print('Saindo do sistema...')

primeiro_contato()
opcao = input("Digite o número da opção desejada: ")

desejaSairDoPrograma=False
while not desejaSairDoPrograma:

    if opcao==1:
        inserir()
    elif opcao==2:
        alterar() 
    elif opcao==3:
        excluir() 
    elif opcao==4:
        listar()
    elif opcao==5:
        medias() #nao ta feito
    else: 
        fechaConexao()
        desejaSairDoPrograma=True