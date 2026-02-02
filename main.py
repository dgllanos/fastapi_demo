from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    """Endpoint raíz que retorna un mensaje de bienvenida"""
    return {"mensaje": "¡Bienvenido a FastAPI!"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    """Endpoint que retorna un item por ID"""
    return {"item_id": item_id, "q": q}


@app.post("/users/")
def create_user(name: str, email: str):
    """Endpoint para crear un usuario"""
    return {"nombre": name, "email": email}
