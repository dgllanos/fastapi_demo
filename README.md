# FastAPI Demo Project

Un proyecto básico con FastAPI para demostrar endpoints simples.

## Instalación

1. Instala las dependencias:
```bash
pip install -r requirements.txt
```

## Ejecución

Para iniciar el servidor:

```bash
uvicorn main:app --reload
```

El servidor estará disponible en `http://127.0.0.1:8000`

## Endpoints disponibles

- `GET /` - Endpoint raíz
- `GET /items/{item_id}` - Obtener un item por ID
- `POST /users/` - Crear un usuario

## Documentación interactiva

Una vez que el servidor esté corriendo, puedes acceder a:
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`
