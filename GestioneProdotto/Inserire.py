from flask import Flask

class Inserire:
    def __init__(self, nome = None, id = None):
        self.__nome = nome
        self.__id = id

    def getNome(self):
        return self.__nome

    def getId(self):
        return self.__id

    def setNome(self, nome):
        self.__nome = nome

    def setId(self, id):
        self.__id = id

