from sqlalchemy import and_
from sqlalchemy.orm import Session
from fastapi import Request, Depends
from fastapi.responses import RedirectResponse
from app.db.models.user import User
from app.utils.password import verify_password

class user_repository:
    @staticmethod
    def login(db: Session, email: str, password: str) -> User | None:
        user = db.query(User).filter(User.email == email).first() #type: ignore
        if user and verify_password(password, user.password):
            return user
        return None

    @staticmethod
    def require_login(request: Request):
        logged_in = request.cookies.get("logged_in")
        if logged_in != "true":
            return RedirectResponse(url="/users/login", status_code=303)