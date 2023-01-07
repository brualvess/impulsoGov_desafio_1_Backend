# A classe Database tem como objetivo centralizar as requisições para o banco de dados
import sqlite3


class Database:
    def __init__(self) -> None:
        self.connection = sqlite3.connect("dados.db")

    async def get_establishments_id(self, id_county):
        cursor = self.connection.cursor()
        get_establishments = """SELECT id_cnes, nome, latitude, longitude 
                                 FROM estabelecimentos WHERE municipio_id_sus = ?
                              """
        cursor.execute(get_establishments, (id_county,))
        establishments = cursor.fetchall()
        return establishments

    async def get_establishment(self, id_cnes):
        cursor = self.connection.cursor()
        get_establishment_by_id_cnes = """SELECT id_cnes, nome, latitude, longitude
                                     FROM estabelecimentos WHERE id_cnes = ?
                                  """
        cursor.execute(get_establishment_by_id_cnes, (id_cnes,))
        establishment = cursor.fetchall()
        return establishment
