from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    # TODO
    def get_all_generi(self):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        cursor.execute("SELECT DISTINCT genere FROM libro")
        result = [row["genere"] for row in cursor]
        cursor.close()
        cnx.close()
        return result

    def get_libri_filtrati(self, nome_biblioteca, genere):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """
            SELECT l.* 
            FROM libro l, biblioteca b
            WHERE l.id_biblioteca = b.id
              AND b.nome = COALESCE(%s, b.nome)
              AND l.genere = COALESCE(%s, l.genere)
        """
        cursor.execute(query, (nome_biblioteca, genere))
        result = []
        for row in cursor:
            result.append(Libro(
                row["id"], row["titolo"], row["autore"],
                row["genere"], row["anno_pubblicazione"], row["id_biblioteca"]
            ))
        cursor.close()
        cnx.close()
        return result
