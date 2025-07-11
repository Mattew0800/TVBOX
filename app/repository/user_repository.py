from sqlalchemy import and_
from sqlalchemy.orm import Session

from app.db.models.user import User
from app.utils.password import verify_password

class user_repository:
    @staticmethod
    def login(db: Session, email: str, password: str) -> User | None:
        user = db.query(User).filter(User.email == email).filter(User.password == password).first() #type: ignore
        return user