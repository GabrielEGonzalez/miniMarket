"""  
* Usuario (id, nombre, email, contraseña)
* `/register` – registrar usuario
* `/login` – login
"""

from fastapi import APIRouter, Depends
from sqlmodel import SQLModel , Session , select , Field
from db import get_session

class Usuario(SQLModel,table=True):
    id : int | None = Field(default=None,primary_key=True)
    nombre: str
    email: str
    password: str


userRouter = APIRouter(prefix="/user", tags=["user"])

@userRouter.post("/register",response_model=Usuario)
async def RegisterUser(usuario: Usuario,session:Session = Depends(get_session)):
    
    try:
        userdb = Usuario.model_validate(usuario)
        session.add(userdb)
        session.commit()
        session.refresh()
        
        return userdb
    except Exception as e :
        return {"error":str(e)}

@userRouter.post("/login")
async def loginUser():
    pass