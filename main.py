from typing import Union
from database import Database
from fastapi import FastAPI

app = FastAPI()
database = Database()


@app.get("/estabelecimentos/listar/{id_county}")
async def listEstablishments(id_county: str):
    establishments = await database.get_establishments_id(id_county)
    response = []
    for establishment in establishments:
        response.append({
            "Código CNES": establishment[0],
            "Nome": establishment[1],
            "Latitude": establishment[2],
            "Longitude": establishment[3]
        })
    return response


@app.get("/estabelecimento/{id_cnes}")
async def get_Establishments_by_id(id_cnes: str):
    establishment = await database.get_establishment(id_cnes)
    establishment_data = establishment[0]
    response = {
        "Código CNES": establishment_data[0],
        "Nome": establishment_data[1],
        "Latitude": establishment_data[2],
        "Longitude": establishment_data[3]
    }
    return response
