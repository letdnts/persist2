from fastapi import APIRouter, HTTPException
from models.voo_model import Voo
from utils.arq_utils import verificar_csv, salvar_voo, listar_voos_csv, atualizar_voo_csv, deletar_voo_csv
import os

voo_router = APIRouter()

@voo_router.post("/voos/")
def inserir_voo(voo: Voo):
    verificar_csv()
    try:
        salvar_voo(voo)
        return {"message": "Voo inserido com sucesso!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao salvar dados: {e}")

@voo_router.get("/voos/")
def listar_voos():
    verificar_csv()
    try:
        voos = listar_voos_csv()
        return voos
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao listar voos: {e}")

@voo_router.get("/voos/{id_voo}")
def obter_voo(id_voo: int):
    verificar_csv()
    try:
        voo = listar_voos_csv(id_voo)
        if not voo:
            raise HTTPException(status_code=404, detail="Voo não encontrado.")
        return voo
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao buscar voo: {e}")

@voo_router.put("/voos/{id_voo}")
def atualizar_voo(id_voo: int, voo_atualizado: Voo):
    verificar_csv()
    try:
        atualizado = atualizar_voo_csv(id_voo, voo_atualizado)
        if not atualizado:
            raise HTTPException(status_code=404, detail="Voo não encontrado.")
        return {"message": "Voo atualizado com sucesso!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao atualizar voo: {e}")

@voo_router.delete("/voos/{id_voo}")
def deletar_voo(id_voo: int):
    verificar_csv()
    try:
        deletado = deletar_voo_csv(id_voo)
        if not deletado:
            raise HTTPException(status_code=404, detail="Voo não encontrado.")
        return {"message": "Voo deletado com sucesso!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao deletar voo: {e}")
