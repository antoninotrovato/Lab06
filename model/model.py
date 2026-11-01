from database.DB_connect import get_connection
from model.strumento import Strumento
from model.prestito import Prestito
import mysql.connector

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def get_strumenti(self) -> list[Strumento] | None:
        """
            Funzione che legge tutti gli strumenti nel database
            :return: una lista con tutti gli strumenti presenti oppure None
        """
        # TODO
        cnx = mysql.connector.connect( user='root',
                                      password='',
                                      host='127.0.0.1',
                                      database='deposito_strumenti',
                                      raise_on_warnings=True)
        query = " SELECT * FROM strumento"
        cursore = cnx.cursor()
        lista_strumenti = []
        cursore.execute(query)
        for riga in cursore:
            strumento = Strumento(
                codice=riga[0],
                tipo=riga[1],
                marca=riga[2],
                anno_acquisto=riga[3],
                valore=riga[4],
                disponibile=riga[5]
            )
            lista_strumenti.append(strumento)
        cursore.close()
        cnx.close()
        if len(lista_strumenti) == 0:
            return None
        return lista_strumenti
    def cerca_strumenti_per_tipo(self, tipo) -> list[Strumento] | None:
        """
            Funzione che recupera una lista con tutti gli strumenti presenti nel database di un certo tipo
            :param tipo: il tipo dello strumento (es. "Chitarra")
            :return: una lista con tutti gli strumenti del tipo indicato oppure None
        """
        # TODO
        cnx = mysql.connector.connect(user='root',
                                      password='',
                                      host='127.0.0.1',
                                      database='deposito_strumenti',
                                      raise_on_warnings=True)

        query = """SELECT * 
                    FROM strumento 
                    WHERE tipo = %s"""
        cursore = cnx.cursor()
        lista_strumenti_per_tipo = []
        cursore.execute(query, (tipo,))
        for riga in cursore:
            strumento = Strumento(
                codice=riga[0],
                tipo=riga[1],
                marca=riga[2],
                anno_acquisto=riga[3],
                valore=riga[4],
                disponibile=riga[5]
            )
            lista_strumenti_per_tipo.append(strumento)
        return lista_strumenti_per_tipo