from typing import Dict, List, Optional
from .schemas import ClienteCreate, ClienteRead

db_clientes: List[ClienteRead] = []
id_counter = 1

def crear(data: ClienteCreate) -> ClienteRead:
    global id_counter
    nuevo = ClienteRead(id = id_counter, **data.model_dump())
    db_clientes.append(nuevo)
    id_counter += 1
    return nuevo

def obtener_todos(skip: int, limit: int) -> List[ClienteRead]:
    return db_clientes[skip : skip + limit]

def obtener_por_id(id: int) -> Optional[ClienteRead]:
    for p in db_clientes:
        if p.id == id:
            return p
    return None

def actualizar_total(id: int, data: ClienteCreate) -> Optional[ClienteRead]:
    for index, p in enumerate(db_clientes):
        if p.id == id:
            cliente_actualizado = ClienteRead(id=id, **data.model_dump())
            db_clientes[index] = cliente_actualizado
            return cliente_actualizado
    return None

def mayor_de_edad(id: int) -> Optional[Dict]:
    for p in db_clientes:
        if p.id == id:
            return {"mayor": p.edad > 17}
    return None