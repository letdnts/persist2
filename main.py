from fastapi import FastAPI
from controllers.voo_controller import voo_router
from controllers.data_controller import arquivo_router

app = FastAPI()

# Incluindo as rotas de voo e arquivo
app.include_router(voo_router)
app.include_router(arquivo_router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Serviço de Gerenciamento de Voos"}
