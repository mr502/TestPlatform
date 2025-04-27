from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TestCaseCreate(BaseModel):
    name: str
    description: Optional[str] = None
    steps: str

class TestCaseOut(TestCaseCreate):
    id: int
    creator_id: int

    class Config:
        orm_mode = True
