from fastapi import FastAPI
from db import engine
from router import Usuario, Carrito, Producto
from sqlmodel import SQLModel


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#crear tablas
@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)


app.include_router(Usuario.userRouter)
app.include_router(Carrito.cardRouter)