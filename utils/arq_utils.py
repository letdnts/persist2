import csv
import os
import hashlib
from fastapi.responses import FileResponse
import zipfile

CSV_FILE = "voos.csv"
HEADER = ["id_voo", "numero_voo", "cia", "origem", 
          "destino", "horario_partida", "horario_chegada", 
          "id_aeronave", "status"]

def verificar_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(HEADER)

def salvar_voo(voo):
    with open(CSV_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            voo.id_voo, voo.numero_voo, voo.cia, voo.origem,
            voo.destino, voo.horario_partida.isoformat(),
            voo.horario_chegada.isoformat(), voo.id_aeronave, voo.status
        ])

def listar_voos_csv(id_voo=None):
    with open(CSV_FILE, "r") as file:
        reader = csv.DictReader(file)
        voos = [
            {key: int(value) if key in ["id_voo", "numero_voo", "id_aeronave"] else value
             for key, value in row.items()}
            for row in reader
        ]
    if id_voo:
        return next((voo for voo in voos if voo['id_voo'] == id_voo), None)
    return voos

def atualizar_voo_csv(id_voo, voo_atualizado):
    voos = []
    atualizado = False
    with open(CSV_FILE, "r") as file:
        reader = csv.DictReader(file, fieldnames=HEADER)
        next(reader, None)
        for row in reader:
            if int(row["id_voo"]) == id_voo:
                voos.append({
                    "id_voo": voo_atualizado.id_voo,
                    "numero_voo": voo_atualizado.numero_voo,
                    "cia": voo_atualizado.cia,
                    "origem": voo_atualizado.origem,
                    "destino": voo_atualizado.destino,
                    "horario_partida": voo_atualizado.horario_partida.isoformat(),
                    "horario_chegada": voo_atualizado.horario_chegada.isoformat(),
                    "id_aeronave": voo_atualizado.id_aeronave,
                    "status": voo_atualizado.status
                })
                atualizado = True
            else:
                voos.append(row)

    if atualizado:
        with open(CSV_FILE, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=HEADER)
            writer.writeheader()
            writer.writerows(voos)
    return atualizado

def deletar_voo_csv(id_voo):
    voos = []
    deletado = False
    with open(CSV_FILE, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if int(row["id_voo"]) == id_voo:
                deletado = True
            else:
                voos.append(row)

    if deletado:
        with open(CSV_FILE, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=HEADER)
            writer.writeheader()
            writer.writerows(voos)
    return deletado

def contar_registros():
    if os.stat(CSV_FILE).st_size == 0:
        return {"Total de Registros": 0}
    with open(CSV_FILE, "r") as file:
        reader = csv.reader(file)
        next(reader, None)
        count = sum(1 for _ in reader)
    return {"Total de Registros": count}

def compactar_csv():
    zip_file = CSV_FILE.replace("voos.csv", "voos.zip")
    with zipfile.ZipFile(zip_file, "w", zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(CSV_FILE, os.path.basename(CSV_FILE))
    return FileResponse(
        path=zip_file,
        media_type="application/zip",
        filename=os.path.basename(zip_file),
    )

def obter_hash():
    with open(CSV_FILE, "rb") as file:
        sha256_hash = hashlib.sha256(file.read()).hexdigest()
    return {"SHA256": sha256_hash}
