from pydantic import BaseModel, Field
from typing import Optional

class ClienteBase(BaseModel):
    nombre: str = Field(..., example="Martin")
    apellido: str = Field(..., example="Carcano")
    edad: int = Field(gt = 0, )
    mail:  str = Field(..., example="martin.carcano@gmail.com")
    
class ClienteCreate(ClienteBase):
    pass

class ClienteUpdate(ClienteBase):
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    edad: Optional[int] = Field(None, ge=0)
    mail:  Optional[str] = None

class ClienteRead(ClienteBase):
    id : int
    
class ClienteMayorEdad(ClienteBase):
    mayor : bool 