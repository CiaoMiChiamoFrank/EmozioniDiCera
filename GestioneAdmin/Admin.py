from flask import Flask

class Admin:
    def __init__(self, nome = None, pwd = None):
        self.__nome = nome
        self.__pwd = pwd

    def get_nome(self):
        return self.__nome

    def get_pwd(self):
        return self.__pwd

    def set_nome(self, nome):
        self.__nome = nome

    def set_pwd(self, pwd):
        self.__pwd = pwd

