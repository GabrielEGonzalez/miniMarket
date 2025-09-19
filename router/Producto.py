from fastapi import APIRouter,Depends,Cookie,HTTPException
from sqlmodel import SQLModel , Field , select, Session
from .Usuario import Usuario 
from db import get_session
from typing import List
class Producto(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nombre: str
    precio: float
    stock: int
    estado: int
    descripcion: str
    
class ProductoRead(SQLModel):
    pass


routerProducto = APIRouter(prefix="/producto",tags=["product"])

@routerProducto.get("/")#,response_model=List[Producto]
async def listaProducto(session: Session = Depends(get_session)):
    try:
        listaproducto = session.exec(select(Producto)).all()
        if listaproducto:
            return listaproducto
        return {"mensaje":"prodcutos no extitente en la base de datos."}
    except Exception as e:
        return {"error":str(e)}
    

@routerProducto.post("/add")
async def addProducto(secret_key = Cookie(),producto:Producto,session : Session = Depends(get_session)):
    
    key = secret_key.split("&")
    user = session.exec(select(Usuario).where(Usuario.email == key[0])).first()
    
    if user.rol == "admin":
        session.add(producto)
        session.commit()
        session.refresh(producto)
    else:
        raise HTTPException(
            status_code=404
            detail={"error":"rol del usuario no permite la accion"}
        )
     
    


"""
  * `/products` – listar productos
  * `/products/add` – agregar producto
"""