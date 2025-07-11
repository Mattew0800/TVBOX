from fastapi import APIRouter, Depends, Request, Form
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserDelete, UserLogin, UserRead, UserUpdate, UserLogin
from app.crud.user import create_user, delete_user, get_user_by_id, get_users, update_user
from app.db.session import get_db
from fastapi.responses import HTMLResponse, RedirectResponse
from app.core.templates import templates  
from app.repository.user_repository import user_repository
from sqlmodel import Session as SQLModelSession




router = APIRouter(prefix="/users", tags=["users"])

@router.post("/create", response_model=UserRead)
def create_user_form(
    request: Request,
    email: str = Form(...),
    first_name: str = Form(...),
    last_name: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    user_data = UserCreate(
        email=email,
        first_name=first_name,
        last_name=last_name,
        password=password
    )
    user = create_user(db, user_data)
 
    return templates.TemplateResponse("success.html", {"request": request, "user": user})


@router.get("/list", response_model=list[UserRead])
def list_users_endpoint(db: Session = Depends(get_db)):
    return get_users(db)

@router.get("/login", response_class=HTMLResponse)
def login_form(request: Request):
    return templates.TemplateResponse("sign_in.html", {"request": request})

@router.get("/{user_id}", response_model=UserRead)
def get_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    return get_user_by_id(db, user_id)

@router.put("/update",response_model=UserRead)
def update_user_endpoint(user: UserUpdate, db: Session = Depends(get_db)):
    return update_user(db, user.id, user)

@router.delete("/delete",response_model="str")
def delete_user_endpoint(user: UserDelete, db: Session = Depends(get_db)):
    return delete_user(db, user.id)

@router.post("/login", response_class=HTMLResponse)
def login_endpoint(
    request: Request,
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    usuario = user_repository.login(db, email, password)
    if usuario:
        return RedirectResponse(url="/users/logueado", status_code=303)
    else:
        return templates.TemplateResponse("sign_in.html", {"request": request, "error": "Credenciales incorrectas"})

@router.get("/logueado", response_class=HTMLResponse)
def logueado(request: Request):
    return templates.TemplateResponse("logueado.html", {"request": request})
