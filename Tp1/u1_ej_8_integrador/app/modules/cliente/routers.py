from fastapi import APIRouter, HTTPException, Path, Query, status
from typing import List
from . import schemas, services

router = APIRouter(prefix="/clientes", tags=["Clientes"])

@router.post(
    "/", response_model=schemas.ClienteRead, status_code=status.HTTP_201_CREATED
)
def alta_cliente(cliente: schemas.ClienteCreate):
    return services.crear(cliente)

@router.get(
    "/", response_model=List[schemas.ClienteRead], status_code=status.HTTP_200_OK
)
def listar_clientes(skip: int = Query(0, ge=0), limit: int = Query(10, le=50)):
    return services.obtener_todos(skip, limit)


# ---------------------------------------------------------
# DETALLE DE CLIENTE
# Método: GET | Endpoint: /clientes/{id} | Estado: 200 OK
# ---------------------------------------------------------
@router.get(
    "/{id}", response_model=schemas.ClienteRead, status_code=status.HTTP_200_OK
)
def detalle_cliente(id: int = Path(..., gt=0)):
    cliente = services.obtener_por_id(id)
    if not cliente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Cliente no encontrado"
        )
    return cliente


# ---------------------------------------------------------
# ACTUALIZACIÓN (Reemplazo Total)
# Método: PUT | Endpoint: /clientes/{id} | Estado: 200 OK
# ---------------------s------------------------------------
@router.put(
    "/{id}", response_model=schemas.ClienteRead, status_code=status.HTTP_200_OK
)
def actualizar_cliente(cliente: schemas.ClienteCreate, id: int = Path(..., gt=0)):
    actualizado = services.actualizar_total(id, cliente)
    if not actualizado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Cliente no encontrado"
        )
    return actualizado

# ---------------------------------------------------------
# MAYOR DE EDAD
# Método: GET | Endpoint: /clientes/mayor/{id} | Estado: 200 OK
# ---------------------------------------------------------
@router.get(
    "/mayor/{id}", response_model=schemas.ClienteMayorEdad, status_code=status.HTTP_200_OK
)
def mayor(id: int = Path(..., gt=0)):
    cliente = services.obtener_por_id(id)
    if not cliente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Cliente no encontrado"
        )
    return {**cliente.model_dump(), "mayor": cliente.edad > 17}