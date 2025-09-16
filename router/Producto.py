from fastapi import FastAPI
from sqlmodel import SQLModel , Field , select

class Producto(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)  # 🔑 PK obligatoria
    nombre: str
    precio: float
    stock: int
    estado: int