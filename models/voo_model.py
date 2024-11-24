from pydantic import BaseModel
from datetime import datetime

class Voo(BaseModel):
    id_voo: int
    numero_voo: int
    cia: str
    origem: str
    destino: str
    horario_partida: datetime
    horario_chegada: datetime
    id_aeronave: int
    status: str
