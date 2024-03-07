CREATE DATABASE IF NOT EXISTS cryptocurrency;

USE cryptocurrency;

CREATE TABLE moedas_info(
idmoedas_info INT PRIMARY KEY NOT NULL auto_increment, 
nome VARCHAR(15) NOT NULL,
tipo_moeda VARCHAR(20) NOT NULL,
data_criacao DATE NOT NULL
);

CREATE TABLE calendario(
idcalendario INT PRIMARY KEY NOT NULL auto_increment,
diasemana CHAR(3),
diames INT NOT NULL,
mes INT NOT NULL,
ano INT NOT NULL
);

CREATE TABLE marketcap_dia(
idmarketcap_dia INT PRIMARY KEY NOT NULL auto_increment,
idmoedas_info INT,
FOREIGN KEY (idmoedas_info) REFERENCES moedas_info(idmoedas_info),
idcalendario INT,
FOREIGN KEY (idcalendario) REFERENCES calendario(idcalendario)
);

CREATE TABLE abrefecha_dia(
idabrefecha_dia INT PRIMARY KEY NOT NULL auto_increment,
valor_abert FLOAT NOT NULL,
valor_fech FLOAT NOT NULL,
idmoedas_info INT,
FOREIGN KEY (idmoedas_info) REFERENCES moedas_info(idmoedas_info),
idcalendario INT,
FOREIGN KEY (idcalendario) REFERENCES calendario(idcalendario)
);

CREATE TABLE minmax_dia(
idminmax_dia INT PRIMARY KEY NOT NULL auto_increment,
max_valor FLOAT NOT NULL,
min_valor FLOAT NOT NULL,
idmoedas_info INT,
FOREIGN KEY (idmoedas_info) REFERENCES moedas_info(idmoedas_info),
idcalendario INT,
FOREIGN KEY (idcalendario) REFERENCES calendario(idcalendario)
);

CREATE TABLE valor_dia(
idvalor_dia INT PRIMARY KEY NOT NULL auto_increment,
idmoedas_info INT,
FOREIGN KEY (idmoedas_info) REFERENCES moedas_info(idmoedas_info),
idmarketcap_dia INT,
FOREIGN KEY (idmarketcap_dia) REFERENCES marketcap_dia(idmarketcap_dia),
idabrefecha_dia INT,
FOREIGN KEY (idabrefecha_dia) REFERENCES abrefecha_dia(idabrefecha_dia),
idminmax_dia INT,
FOREIGN KEY (idminmax_dia) REFERENCES minmax_dia(idminmax_dia),
idcalendario INT,
FOREIGN KEY (idcalendario) REFERENCES calendario(idcalendario)
);

