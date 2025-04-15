create database projeto_sustentabilidade;

use projeto_sustentabilidade;
#  criando tabela de verificador de sustentabilidade
create table verficador(
codigo int not null auto_increment,
data date,
qtd_de_agua_litros decimal(10,2),
uso_energia_eletrica_kwh decimal(10,2),
residuos_nao_reciclaveis_kg DECIMAL(10,2),
porcentagem_de_reciclado_hoje DECIMAL(5,2),
transporte_publico enum('Sim','Nao'),
bicicleta enum('Sim','Nao'),
caminhada enum('Sim','Nao'),
carro enum('Sim','Nao'),
carro_eletrico enum('Sim','Nao'),
carona enum('Sim','Nao'),
primary key (codigo)
);
#exibir tabela
select * from verficador;
describe verficador;
#INSERINDO VALORES PARA EXEMPLOS (TESTE)a

INSERT INTO projeto_sustentabilidade.verficador
(codigo,data,qtd_de_agua_litros,uso_energia_eletrica_kwh,residuos_nao_reciclaveis_kg,porcentagem_de_reciclado_hoje,transporte_publico ,bicicleta,caminhada,carro,carro_eletrico,carona )
values
(1,'2025-04-13',1500.0,30.5,10.2,45.50,'Sim','Nao','Sim','Nao','Sim','Nao');
