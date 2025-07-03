from fastapi import FastAPI
from app.api.v1.enpoints.users import router as users_router
from app.db.models.user import User
from app.db.session import engine

app = FastAPI()

# Crear tablas si no existen
User.metadata.create_all(engine)

app.include_router(users_router)
