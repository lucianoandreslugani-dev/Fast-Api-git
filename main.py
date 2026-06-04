
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

@app.get("/productos/{id}")
def actualizar_producto(id: int, producto: Producto):
    if id < 0 or id >= len(productos):
        return {"error": "Producto no encontrado"}

    return {"mensaje": "Producto encotrado correctamente", "producto": producto}



@app.post("/productos")
def agregar_producto(producto: Producto):
    productos.append(producto)
    return {"mensaje": f"Producto agregado correctamente", "producto": producto}


@app.put("/productos/{id}")
def actualizar_producto(id: int, producto: Producto):
    if id < 0 or id >= len(productos):
        return {"error": "Producto no encontrado"}
    productos[id] = producto
    return {"mensaje": "Producto actualizado correctamente", "producto": producto}


