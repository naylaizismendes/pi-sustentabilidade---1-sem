from copy import Error
import mysql.connector

#ao entrar no programa 
def primeiro_contato ():
   print(" _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
   print("|                                                               |")
   print("|     Sistema de Monitoramento de Sustentabilidade Pessoal      |")        
   print("|_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|")
   print("|                                                               |")
   print("| 1. Inserir dados de monitoramento                             |") 
   print("| 2. Alterar dados de monitoramento                             |") 
   print("| 3. Apagar dados de monitoramento                              |") 
   print("| 4. Listar cada monitoramento diário e classificar             |") #arrumar  
   print("| 5. Calcular e mostrar as médias dos parâmetros e classificar  |") #terminar
   print("| 6. Sair do sistema                                            |")
   print("|_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|")
   print()
   

#conexao  
def obtemConexao (servidor, usuario, senha, bd):
    if obtemConexao.conexao==None:
        obtemConexao.conexao = mysql.connector.connect(host    =f"{servidor}",\
                                                       user    =f"{usuario}",\
                                                       password=f"{senha}",\
                                                       database=f"{bd}")

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

   conexao=obtemConexao("localhost","root","saopaulo","projeto_sustentabilidade")
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

   insercao_dados(data, qtd_de_agua_litros, uso_energia_eletrica_kwh,
            residuos_nao_reciclaveis_kg, porcentagem_de_reciclado_hoje,
            transportePublico, bicicleta, caminhada, carro,
            carroEletrico, carona)
   
   print("Dados inseridos com sucesso!")
   return
primeiro_contato()
#atualizar uma informação
def alterar ():
   while True:
      data_atualizar = input("Digite a data que deseja alterar (AAAA-MM-DD): ")
      try:
         data_atualizar = datetime.strptime(data_atualizar, "%d%m%Y").date()
         break
      except ValueError:
         print("Data inválida. Por favor, insira no formato DDMMYYYY.")
      
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

   comando = f"UPDATE verficador SET {dados[dados_opcao]} = '{novo_valor}' WHERE data = '{data_atualizar}'"
  

   try:
      conexao=obtemConexao("localhost","root","saopaulo","projeto_sustentabilidade")
      cursor = conexao.cursor()
      cursor.execute(comando)
      conexao.commit()
      print("Informação atualizada com sucesso.")
   except Error as e:
      print(f"Erro ao atualizar: {e}")
   
   return
def excluir ():
   confirmacao = input('Tem certeza que deseja excluir um registro? ').upper()
   while confirmacao not in ('S', 'N'):
      print('Resposta inválida. Por favor, digite S ou N.')
      confirmacao = input('Tem certeza que deseja excluir um registro? ').upper()
   
   if confirmacao == 'S':
      while True:
         data_excluir = input("Digite a data que deseja deletar: ")
         try:
            data_excluir = datetime.strptime(data_excluir, "%d%m%Y").date()
            break
         except ValueError:
            print("Data inválida. Por favor, insira no formato DDMMYYYY.")

      comando = f"DELETE FROM verficador WHERE data = '{data_excluir}'"
      conexao=obtemConexao("localhost","root","saopaulo","projeto_sustentabilidade")
      cursor=conexao.cursor()
      cursor.execute(comando)
      conexao.commit()
      print("Registro deletado com sucesso!\n")

def listagem ():
    comando= "Select DATE_FORMAT(data,'%d/%m/%Y'), qtd_de_agua_litros, uso_energia_eletrica_kwh, residuos_nao_reciclaveis_kg, porcentagem_de_reciclado_hoje, transporte_publico, bicicleta, caminhada, carro,  carro_eletrico, carona FROM verficador"
    conexao=obtemConexao("localhost","root","saopaulo","projeto_sustentabilidade")
    cursor=conexao.cursor()
    cursor.execute(comando)

    linhas=cursor.fetchall()
    return linhas

#lista todos os registros  
def listar (): 
    try:
        linha=listagem()
    except Error:    
        print("Problema de conexão com o BD!")
    else:
        atual=0
        while atual<len(linha):
            print()
            print('Data.......:',linha[atual][0])
            print('Qtd de água:',linha[atual][1])
            print('Qtd energia:',linha[atual][2])
            print('Residuos não reciclaveis:',linha[atual][3])
            print('reciclados :',linha[atual][4])
            print('Transporte publico:',linha[atual][5])
            print('bicicleta:',linha[atual][6])
            print('caminhada:',linha[atual][7])
            print('carro:',linha[atual][8])
            print('carro eletrico:',linha[atual][9])
            print('carona:',linha[atual][10])
            atual+=1

        print()
        print("Listagem concluida com sucesso!")
     

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
#media para transportes em geral(publico, eletrico e fosseis)
   
   cursor.execute("""
        SELECT 
            SUM(transporte_publico = 'S') +
            SUM(bicicleta = 'S') +
            SUM(caminhada = 'S') +
            SUM(carro_eletrico = 'S') AS sustentavel,
            
            SUM(carro = 'S') +
            SUM(carona = 'S') AS nao_sustentavel
        FROM verficador
    """)

 
  
   resultado = cursor.fetchone()
   sustentavel, nao_sustentavel = resultado

   print(f"Total sustentável: {sustentavel}")
   print(f"Total não sustentável: {nao_sustentavel}")

   if sustentavel > nao_sustentavel:
        print("Transporte: Alta sustentabilidade")
   elif sustentavel == nao_sustentavel:
        print("Transporte: Sustentabilidade moderada")
   else:
        print("Transporte: Baixa sustentabilidade")

   cursor.close()
         
def fechaConexao ():
    conexao=obtemConexao("localhost","root","saopaulo","projeto_sustentabilidade")
    cursor=conexao.cursor()
    cursor.close()
    conexao.close()
   



desejaSairDoPrograma=False
while not desejaSairDoPrograma:
   digitou_corretamente = False
   while not digitou_corretamente:
      try:
         primeiro_contato()
         opcao = int(input("Digite o número da opção desejada: "))
      except ValueError:
         print("Digite apenas números; tente novamente!")
      else:
         if opcao <= 0 or opcao > 6:
            print("Não existe essa opção; tente novamente!")
         else:
            digitou_corretamente=True

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


print()        
print('PROGRAMA ENCERRADO; OBRIGADO POR USAR ESTE SISTEMA DE MONITORAMENTO PESSOAL DE SUSTENTABILIDADE!')