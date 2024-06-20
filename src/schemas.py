from datetime import date
from typing import Optional
from pydantic import BaseModel, Field, EmailStr, PastDate

class UserSchema(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(min_length=6, max_length=8)


class UserResponse(BaseModel):
    id: int = 1
    username: str
    avatar: str
    email: EmailStr

    class Config:
        from_attributes = True


class RequestEmail(BaseModel):
    email: EmailStr

class NoteBase(BaseModel):
    name: str = Field(max_length=50)
    familyname: str = Field(max_length=50)
    email: EmailStr
    phone: str = Field(min_length=10,max_length=10, default="0123456789")
    birthday: PastDate = None
    other: Optional[str] = None
    bd_soon: bool = False

class NoteModel(NoteBase):
    pass

class NoteResponse(NoteBase):
    id: int
    user: UserResponse | None

    class Config:
        from_attributes = True



class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"