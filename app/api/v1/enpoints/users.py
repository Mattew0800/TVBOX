from fastapi import APIRouter, Depends, Request, Form, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserDelete, UserLogin, UserRead, UserUpdate, UserLogin
from app.crud.user import create_user, delete_user, get_user_by_id, get_users, update_user
from app.db.session import get_db
from fastapi.responses import HTMLResponse, RedirectResponse
from app.core.templates import templates  
from app.repository.user_repository import user_repository
from sqlmodel import Session as SQLModelSession
from app.db.models.user import User
from app.db.models.user import UserGridConfig
from datetime import datetime




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
    try:
        user_data = UserCreate(
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password
        )
        user = create_user(db, user_data)
    
        return templates.TemplateResponse("success.html", {"request": request, "user": user})
    except ValueError as e:
                return templates.TemplateResponse(
            "create_user.html",
            {
                "request": request,
                "error": str(e),
                "email": email,
                "first_name": first_name,
                "last_name": last_name
            }
        )



@router.get("/list", response_model=list[UserRead])
def list_users_endpoint(db: Session = Depends(get_db)):
    return get_users(db)

@router.get("/login", response_class=HTMLResponse)
def login_form(request: Request):
    return templates.TemplateResponse("sign_in.html", {"request": request})


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
        response = RedirectResponse(url="/users/logueado", status_code=303)
        response.set_cookie(key="logged_in", value="true")
        response.set_cookie(key="user_email", value=email)
        return response
    else:
        return templates.TemplateResponse("sign_in.html", {"request": request, "error": "Credenciales incorrectas"})


@router.get("/logueado", response_class=HTMLResponse)
def logueado(request: Request, login_check=Depends(user_repository.require_login), db: Session = Depends(get_db)):
    # Si la dependencia retorna una respuesta, FastAPI la usa directamente
    if isinstance(login_check, RedirectResponse):
        return login_check
    # Obtener usuario actual por email de la cookie o sesión (aquí ejemplo simple)
    user_email = request.cookies.get('user_email')
    user = None
    user_id = None
    if user_email is not None and isinstance(user_email, str) and '@' in user_email:
        user = db.query(User).filter(User.email == str(user_email)).first() #type: ignore
        if user:
            user_id = user.id
    config = db.query(UserGridConfig).filter(UserGridConfig.user_id == user_id).first()
    config_json = config.config_json if config else None
    return templates.TemplateResponse(
        "logueado.html",
        {
            "request": request,
            "user_id": user_id,
            "grid_config": config_json
        }
    )


@router.get("/tvbox_4", response_class=HTMLResponse)
def tvbox_4(request: Request):
    return templates.TemplateResponse("tvbox_4.html", {"request": request})


@router.post("/save_grid_config")
def save_grid_config(request: Request, user_id: int = Form(...), config_json: str = Form(...), db: Session = Depends(get_db)):
    """Guarda o actualiza la configuración de grillas/videos para el usuario actual."""
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    config = db.query(UserGridConfig).filter(UserGridConfig.user_id == user_id).first() #type: ignore
    if config:
        config.config_json = config_json
        config.updated_at = datetime.utcnow()
    else:
        config = UserGridConfig(user_id=user_id, config_json=config_json)
        db.add(config)
    db.commit()
    return {"status": "ok"}

@router.get("/get_grid_config")
def get_grid_config(user_id: int, db: Session = Depends(get_db)):
    """Devuelve la configuración de grillas/videos del usuario actual, si existe."""
    config = db.query(UserGridConfig).filter(UserGridConfig.user_id == user_id).first() #type: ignore
    if config:
        return {"config_json": config.config_json}
    else:
        return {"config_json": None}

@router.get("/logout")
def logout():
    response = RedirectResponse(url="/users/login", status_code=303)
    response.delete_cookie("logged_in")
    response.delete_cookie("user_email")
    return response

@router.get("/{user_id}", response_model=UserRead)
def get_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    return get_user_by_id(db, user_id)


