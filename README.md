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

## Docker

Construir la imagen Docker:

```bash
docker build -t fastapi-demo:latest .
```

Ejecutar la imagen localmente (usa la variable `PORT` si quieres otro puerto):

```bash
docker run -p 8000:8000 -e PORT=8000 fastapi-demo:latest
```

Accede a `http://127.0.0.1:8000` o la documentación en `/docs`.

## Notas para ECS

- Sube la imagen a Amazon ECR y utiliza el repositorio ECR como fuente de imagen en tu Task Definition.
- Asegúrate de configurar el puerto de contenedor `8000` en la definición de la tarea.
- Para producción considera usar un proceso manager o Gunicorn con Uvicorn workers, pero `uvicorn` es suficiente para testing y ejemplos.

Ejemplo rápido para subir a ECR (resumen):

```bash
# 1) Autenticar docker en ECR
aws ecr get-login-password --region <region> | docker login --username AWS --password-stdin <aws_account_id>.dkr.ecr.<region>.amazonaws.com

# 2) Construir y etiquetar
docker build -t fastapi-demo:latest .
docker tag fastapi-demo:latest <aws_account_id>.dkr.ecr.<region>.amazonaws.com/fastapi-demo:latest

# 3) Push
docker push <aws_account_id>.dkr.ecr.<region>.amazonaws.com/fastapi-demo:latest
```

Reemplaza `<region>` y `<aws_account_id>` por tus valores.
