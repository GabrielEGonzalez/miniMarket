from fastapi import APIRouter, Depends, Response, status
from sqlmodel import Field, SQLModel, create_engine, Session, select , Field
from db import get_session
from .Producto import Producto
from pydantic import BaseModel
from typing import List

class Carrito(SQLModel, table=True):
    id: int | None = Field(default=None,primary_key=True)
    usuario_id: int 
    producto_id: int


class Carritoread(BaseModel):
    id:int
    usuario_id:int
    productos: List[Producto] = []


cardRouter = APIRouter(prefix="/product",tags=["product"])
# /cart  ver carrito
# /cart/add  agregar producto al carrito
@cardRouter.get("/getProduct/{id_user}",response_model=list[Carritoread],status_code=status.HTTP_200_OK)
async def getCard(id_user: int, session: Session = Depends(get_session)):
    
    try:
        
        listaProducto = []
        carrito = session.exec(select(Carrito).where(Carrito.usuario_id == id_user)).all()
        for card in carrito:
            x = session.exec(select(Producto).where(Producto.id == card.producto_id)).first()
            if x:
                listaProducto.append(Carritoread(id=card.id,usuario_id= card.usuario_id, productos = [x]))
  
        return listaProducto
    except Exception as e:
        return {"error": str(e)}

@cardRouter.post("/add/producto")
async def addProducto(carrito: Carrito , session: Session = Depends(get_session)):
    try:

        db_addCard = Carrito.model_validate(carrito)
        session.add(db_addCard)
        session.commit()
        session.refresh(db_addCard)
        return db_addCard
    except Exception as e:
        return {"error": str(e)}



"""
Separar modelos:

    Usa un modelo de base de datos (Producto, Carrito) solo para ORM.

    Usa modelos de respuesta (ProductoRead, CarritoRead) para lo que devuelve la API.

Endpoints consistentes:

    GET carrito devuelve CarritoRead con lista de ProductoRead.

    POST al carrito devuelve el mismo formato para mantener consistencia.

Validaciones claras:

    No exponer campos sensibles del producto (ej. costos internos) en la respuesta.

    Validar existencia de usuario y producto antes de agregar al carrito.

Muchos a muchos:

    Cada fila de Carrito representa un producto vinculado a un usuario.
    Mantener relación simple y escalable, no guardar lista de productos en un solo registro.

Preparar para producción:

    Añadir manejo de errores consistente.
    Documentar correctamente en Swagger.
    Mantener los routers organizados por entidad (users, products, cart).
"""