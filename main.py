
from fastapi import FastAPI
from pydantic import BaseModel

app= FastAPI()
productos = []
class Producto(BaseModel):
    nombre: str
    precio: float
    en_stock: bool

@app.get("/productos")
def listar_productos():
    return {"productos": productos}


@app.post("/productos")
def agregar_producto(producto: Producto):
    productos.append(producto)
    return {"mensaje": f"Producto agregado correctamente", "producto": producto}

