print('Seja bem-vindo ao Sistema de Monitoramento de sustentbilidade')

try:
   data=int(input('Digite a data atual: \n '))
except ValueError:
   print('Invalido,Valor deve ser numerico ')
try:
   qtd_de_agua_litros=float(input('Quantos lintros de água você consumiu hoje: \n'))
except ValueError:
   print('Ivalido,valor deve ser numerico!')


try:
   uso_energia_eletrica_kwh=float(input('Quantos kWh de energia eletrica voce consumiu hoje: \n'))
except ValueError:
    print('Ivalido, valor deve ser numerico !')

try: 
   residuos_nao_reciclaveis_kg=float(input('Quantos kg de resiudos não reciclaveis voce gerou hoje: \n'))
except ValueError:
   print('Ivalido, valor deve ser numerico!')

try:
   porcentagem_de_reciclado_hoje= float(input('Qual e a porcentagem de residuos reciclados no total em (%): \n'))
except ValueError:
    print( 'Ivalido, valor deve ser numerico')


