print('Seja bem-vindo ao Sistema de Monitoramento de Sustentabilidade')


data=input('Digite a data atual: ')

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
      residuos_nao_reciclaveis_kg=float(input('Quantos kg de resíduos não recicláveis você gerou hoje: '))
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

transportePublico = input('1. Transporte público (Ônibus,metrô, trem): ').upper()
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

carroEletrico = input('5. Carro elétrico: ').upper()
while carroEletrico not in ('S', 'N'):
    print('Resposta inválida. Por favor, digite S ou N.')
    carroEletrico = input('5. Carro elétrico: ').upper()

carona = input('6. Carona compartilhada (Fósseis): ').upper()
while carona not in ('S', 'N'):
    print('Resposta inválida. Por favor, digite S ou N.')
    carona = input('6. Carona compartilhada (Fósseis): ').upper()


# Verifica o consumo de água
if qtd_de_agua_litros < 150:
   print('Consumo de Água: Alta sustentabilidade')
elif qtd_de_agua_litros >= 150 and qtd_de_agua_litros <= 200:
   print('Consumo de Água: Moderada sustentabilidade')
else:
   print('Consumo de Água: Baixa sustentabilidade')

# Verifica o consumo de energia
if uso_energia_eletrica_kwh < 5:
   print('Consumo de Energia Elétrica: Alta sustentabilidade')
elif uso_energia_eletrica_kwh >= 5 and uso_energia_eletrica_kwh <= 10:
   print('Consumo de Energia Elétrica: Moderada sustentabilidade')
else:
   print('Consumo de Energia Elétrica: Baixa sustentabilidade')
   
# Verifica a geração de resíduos não reciclaveis 
if porcentagem_de_reciclado_hoje < 20:
   print('Porcentagem de resíduos reciclados: Baixa sustentabilidade')
elif porcentagem_de_reciclado_hoje >= 20 and porcentagem_de_reciclado_hoje <= 50:
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
