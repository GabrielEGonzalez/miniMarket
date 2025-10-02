"""  
* Usuario (id, nombre, email, contraseña)
* `/register`  registrar usuario
* `/login`  login
"""

from fastapi import APIRouter, Depends , Response
from sqlmodel import SQLModel , Session , select , Field
from db import get_session

class Usuario(SQLModel,table=True):
    id : int | None = Field(default=None,primary_key=True)
    nombre: str
    email: str
    password: str
    rol:str


userRouter = APIRouter(prefix="/user", tags=["user"])

@userRouter.post("/register",response_model=Usuario)
async def RegisterUser(
                    usuario: Usuario,
                    response: Response,
                    session:Session = Depends(get_session)
):
    
    try:
        userdb = Usuario.model_validate(usuario)
        secret=f"{usuario.id}&{usuario.email}&{usuario.rol}"
        session.add(userdb)
        session.commit()
        session.refresh(userdb)
        response.set_cookie(key="secret_key",value=secret)
        return userdb
    except Exception as e :
        return {"error":str(e)}

@userRouter.post("/login")
async def loginUser(
    usuariologin: Usuario, 
    response: Response, 
    session:Session=Depends(get_session)
):
    try:
        user = session.exec(select(Usuario).where(Usuario.email==usuariologin.email)).first()
        if user:
            secret = f"{user.id}&{user.email}&{user.rol}"
            response.set_cookie(key="secret_key",value=secret)
            return user
        else:
            return {"text":"usuario no existen en los registro"}
    except Exception as e:
        return {"error":str(e)}