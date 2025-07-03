from sqlmodel import SQLModel
from typing import Optional

class UserCreate(SQLModel):
    email: str
    first_name: str
    last_name: str
    password: str

class UserRead(SQLModel):
    id: int
    email: str
    first_name: str
    last_name: str

class UserUpdate(SQLModel):
    id:int
    email: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    password: Optional[str] = None


class UserDelete(SQLModel):
    id:int


