from fastapi import FastAPI
from app.routes import router

app = FastAPI()

# Incluir las rutas definidas en routes.py
app.include_router(router)
