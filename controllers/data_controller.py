from fastapi import APIRouter, HTTPException
from utils.arq_utils import compactar_csv, obter_hash, contar_registros

arquivo_router = APIRouter()

@arquivo_router.get("/contar_registros")
def contar_registros_endpoint():
    try:
        return contar_registros()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao contar registros: {e}")

@arquivo_router.get("/voos/compactar")
def compactar_csv_endpoint():
    try:
        return compactar_csv()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao compactar arquivo: {e}")

@arquivo_router.get("/hash/")
def obter_hash_endpoint():
    try:
        return obter_hash()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao calcular hash: {str(e)}")
