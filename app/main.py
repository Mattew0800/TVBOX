from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from app.api.v1.enpoints.users import router as users_router
from app.db.models.user import User
from app.db.session import engine
from app.core.templates import templates

app = FastAPI()

# Montar archivos estáticos (CSS, JS)
app.mount("/static", StaticFiles(directory="app/templates/static"), name="static")


# Crear tablas si no existen
User.metadata.create_all(engine)

app.include_router(users_router)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("create_user.html", {"request": request})