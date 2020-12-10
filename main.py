from db.reserva_db import ReservaInDB
from db.reserva_db import update_reserva, get_reserva, database_reservas
from models.reserva_models import ReservaIn, ReservaOut

from fastapi import FastAPI, HTTPException

api = FastAPI()

@api.get("/reserva/vista/{num_reserva}")
async def listar_reserva(num_reserva: str):

    reserva_in_db = get_reserva(num_reserva)

    if reserva_in_db == None:
        raise HTTPException(status_code=404, detail="La reserva no existe")

    
    reserva_out = ReservaOut(**reserva_in_db.dict())

    return  reserva_out

@api.post("/reserva/crear")
async def crear_reserva(reserva:ReservaInDB):
    database_reservas[reserva.num_reserva]=reserva
    return reserva