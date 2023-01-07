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
