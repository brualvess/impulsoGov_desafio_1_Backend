from typing import Union
from database import Database
from fastapi import FastAPI
from fastapi import FastAPI, HTTPException

app = FastAPI()
database = Database()


@app.get("/estabelecimentos/listar/{id_county}")
async def list_establishments(id_county: str):
    establishments = await database.get_establishments_id(id_county)
    response = []
    if len(establishments) == 0:
        raise HTTPException(status_code=404)
    else:
        for establishment in establishments:
            response.append({
                "Código CNES": establishment[0],
                "Nome": establishment[1],
                "Latitude": establishment[2],
                "Longitude": establishment[3]
            })
    return response


@app.get("/estabelecimento/{id_cnes}")
async def get_establishments_by_id(id_cnes: str):
    establishment = await database.get_establishment(id_cnes)
    establishment_data = establishment[0]
    if len(establishment) == 0:
        raise HTTPException(status_code=404)
    else:
        response = {
            "Código CNES": establishment_data[0],
            "Nome": establishment_data[1],
            "Latitude": establishment_data[2],
            "Longitude": establishment_data[3]
        }
    return response
