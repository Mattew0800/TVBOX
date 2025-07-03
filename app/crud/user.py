from sqlalchemy.orm import Session
from app.db.models.user import User
from app.schemas.user import UserCreate, UserUpdate

def create_user(db: Session, user: UserCreate) -> User:
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session):
    return db.query(User).all()


def get_user_by_id(db: Session, user_id: int) -> User | None:
    return db.query(User).filter(User.id == user_id).first()  # type: ignore


def update_user(db: Session, user_id: int, user_update: UserUpdate) -> User | None:
    db_user = db.query(User).filter(User.id == user_id).first()  # type: ignore
    if not db_user:
        return None
    for key, value in user_update.dict(exclude_unset=True).items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int) -> str:
    db_user = db.query(User).filter(User.id == user_id).first() # type: ignore
    if not db_user:
        return "Usuario no encontrado"
    db.delete(db_user)
    db.commit()
    return "Eliminado correctamente"
