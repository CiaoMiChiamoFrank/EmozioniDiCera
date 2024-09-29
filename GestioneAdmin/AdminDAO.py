from .Admin import Admin
from DBConnection.GestioneConnessione import GestioneConnessione
from GestioneProdotto.Prodotto import Prodotto
from GestioneProdotto.Inserire import Inserire

class AdminDAO:

    def __init__(self):
        self.__gestioneConnessione = GestioneConnessione()
        self.__connection = self.__gestioneConnessione.getConnessione()
        self.__cursor = self.__gestioneConnessione.getCursor()

    def CreateProdotto (self, prodotto):
        query = """
            INSERT INTO Prodotto (nome, descrizione, prezzo)
            VALUES ( %s, %s, %s)
        """
        print("DAO ciao")
        values = ( prodotto.get_nome(), prodotto.get_descrizione(), prodotto.get_prezzo())

        print(values)
        self.__cursor.execute(query, values)
        self.__connection.commit() # Essenziale, Commit della transazione

