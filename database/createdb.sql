CREATE DATABASE IF NOT EXISTS cryptocurrency;

USE cryptocurrency;

CREATE TABLE moedas_info(
idmoedas_info INT PRIMARY KEY NOT NULL auto_increment, 
nome VARCHAR(15) NOT NULL,
tipo_moeda VARCHAR(20) NOT NULL,
data_criacao DATE NOT NULL
);

CREATE TABLE marketcap_dia(
idmarketcap_dia INT PRIMARY KEY NOT NULL auto_increment,
FOREIGN KEY (idmoedas_info) REFERENCES moedas_info(idmoedas_info)
);

CREATE TABLE abrefecha_dia(
idabrefecha_dia INT PRIMARY KEY NOT NULL auto_increment,
valor_abert FLOAT NOT NULL,
valor_fech FLOAT NOT NULL,
FOREIGN KEY (idmoedas_info) REFERENCES moedas_info(idmoedas_info)
);

CREATE TABLE minmax_dia(
idminmax_dia INT PRIMARY KEY NOT NULL auto_increment,
max_valor FLOAT NOT NULL,
min_valor FLOAT NOT NULL,
FOREIGN KEY (idmoedas_info) REFERENCES moedas_info(idmoedas_info)
);

CREATE TABLE valor_dia(
idvalor_dia INT PRIMARY KEY NOT NULL auto_increment,
FOREIGN KEY (idmoedas_info) REFERENCES moedas_info(idmoedas_info),
FOREIGN KEY (idmarketcap_dia) REFERENCES marketcap_dia(idmarketcap_dia),
FOREIGN KEY (idminmax_dia) REFERENCES abrefecha_dia(idminmax_dia),
FOREIGN KEY (idminmax_dia) REFERENCES minmax_dia(idminmax_dia)
);
