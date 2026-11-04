from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    # TODO
    def get_all_biblioteche(self):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        cursor.execute("SELECT * FROM biblioteca")
        result = []
        for row in cursor:
            result.append(Biblioteca(row["id"], row["nome"], row["indirizzo"]))
        cursor.close()
        cnx.close()
        return result
