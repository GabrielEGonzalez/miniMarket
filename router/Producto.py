from fastapi import APIRouter
from sqlmodel import SQLModel , Field , select
from db import 
class Producto(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nombre: str
    precio: float
    stock: int
    estado: int
    
class ProductoRead(SQLModel):
    pass


routerProducto = APIRouter(prefix="/producto",tags=["product"])

@routerProducto.get("/")
async def listaProducto():
    pass
    

@routerProducto.post("/add")
async def addProducto():
    pass


"""
  * `/products` – listar productos
  * `/products/add` – agregar producto
"""