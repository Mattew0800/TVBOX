from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from datetime import datetime
from sqlalchemy import Text, Column

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    email: str
    first_name: str
    last_name: str
    password: str

class UserGridConfig(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    config_json: str = Field(sa_column=Column(Text))
    updated_at: Optional[datetime] = Field(default_factory=datetime.utcnow)
