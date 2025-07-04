from fastapi import APIRouter, Depends, Request, Form
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserDelete, UserRead, UserUpdate
from app.crud.user import create_user, delete_user, get_user_by_id, get_users, update_user
from app.db.session import get_db
from fastapi.responses import HTMLResponse
from app.core.templates import templates  




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
 # Aquí puedes crear el usuario como antes
    user_data = UserCreate(
        email=email,
        first_name=first_name,
        last_name=last_name,
        password=password
    )
    user = create_user(db, user_data)
    # Puedes renderizar una plantilla de éxito o redirigir
    return templates.TemplateResponse("success.html", {"request": request, "user": user})

    

@router.get("/list", response_model=list[UserRead])
def list_users_endpoint(db: Session = Depends(get_db)):
    return get_users(db)

@router.get("/{user_id}", response_model=UserRead)
def get_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    return get_user_by_id(db, user_id)

@router.put("/update",response_model=UserRead)
def update_user_endpoint(user: UserUpdate, db: Session = Depends(get_db)):
    return update_user(db, user.id, user)

@router.delete("/delete",response_model="str")
def delete_user_endpoint(user: UserDelete, db: Session = Depends(get_db)):
    return delete_user(db, user.id)
