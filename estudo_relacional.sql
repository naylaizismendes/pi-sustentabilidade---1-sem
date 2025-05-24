create database loja;
use loja;
create table produto(
	id_produto int auto_increment primary key,
    nome varchar (50) not null,
    preco_produto decimal (10,2)
);