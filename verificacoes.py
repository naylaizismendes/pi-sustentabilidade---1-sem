print('Seja bem-vindo ao Sistema de Monitoramento de sustentbilidade')


data=input('Digite a data atual: ')

validador = False
while not validador:
   try:
      qtd_de_agua_litros=float(input('Quantos lintros de água você consumiu hoje: '))
   except ValueError:
      print('Invalido, o valor deve ser numerico, Tente novamente!')
   else:
      validador = True
      
validador = False
while not validador:
   try:
      uso_energia_eletrica_kwh=float(input('Quantos kWh de energia eletrica voce consumiu hoje: '))
   except ValueError:
      print('Invalido, o valor deve ser numerico, Tente novamente!')
   else:
      validador = True

validador = False
while not validador:
   try: 
      residuos_nao_reciclaveis_kg=float(input('Quantos kg de resiudos não reciclaveis voce gerou hoje: '))
   except ValueError:
      print('Invalido, o valor deve ser numerico, Tente novamente!')
   else: 
      validador = True

validador = False
while not validador:
   try:
      porcentagem_de_reciclado_hoje= float(input('Qual e a porcentagem de residuos reciclados no total em (%): '))
   except ValueError:
      print('Invalido, o valor deve ser numerico, Tente novamente!')
   else:
      validador = True
    
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
