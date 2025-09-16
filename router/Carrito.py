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
@cardRouter.get("/produto/{id_user}",response_model=list[Carritoread],status_code=status.HTTP_200_OK)
async def getCard(id_user: int, session: Session = Depends(get_session)):
    
    try:
        producto = session.exec(select(Carritoread).where(Carritoread.id == id_user)).all()
        return producto
    except Exception as e:
        return {"error": str(e)}

@cardRouter.post("/add/producto")
async def addProducto(session: Session = Depends(get_session)):
    try:
        carrito = Carrito()  
        db_addCard = Carrito.model_validate(carrito)
        session.add(db_addCard)
        session.commit()
        session.refresh(db_addCard)
        return db_addCard
    except Exception as e:
        return {"error": str(e)}