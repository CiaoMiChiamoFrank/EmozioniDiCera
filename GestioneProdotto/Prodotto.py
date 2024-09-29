from flask import Flask

class Prodotto:
    def __init__(self, id, nome = None, descrizione = None, prezzo = None):
        self.__id = id
        self.__nome = nome
        self.__descrizione = descrizione
        self.__prezzo = prezzo

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_descrizione(self):
        return self.__descrizione

    def get_prezzo(self):
        return self.__prezzo

    def set_id(self, id):
        self.__id = id

    def set_nome(self, nome):
        self.__nome = nome

    def set_descrizione(self, descrizione):
        self.__descrizione = descrizione

    def set_prezzo(self, prezzo):
        self.__prezzo = prezzo
