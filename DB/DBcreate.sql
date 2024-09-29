DROP database EmozioniDiCera;
CREATE DATABASE EmozioniDiCera;

USE EmozioniDiCera;

CREATE TABLE admin (
    nome VARCHAR(50) NOT NULL primary key,
    pwd VARCHAR(50) NOT NULL
);

CREATE TABLE prodotto(
	id BIGINT AUTO_INCREMENT NOT NULL primary key,
    nome VARCHAR(50) NOT NULL,
    descrizione VARCHAR(250) NOT NULL,
    prezzo DOUBLE NOT NULL
);

CREATE TABLE inserire(
	nome VARCHAR(50) NOT NULL,
    id BIGINT NOT NULL,
    PRIMARY KEY (nome, id),
    FOREIGN KEY (nome) REFERENCES admin(nome),
    FOREIGN KEY (id) REFERENCES prodotto(id)
);

