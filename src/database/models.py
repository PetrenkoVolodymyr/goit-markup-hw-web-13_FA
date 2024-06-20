from sqlalchemy import Column, Integer, String, Boolean, func, ForeignKey
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Note(Base):
    __tablename__ = "notes"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    familyname = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)
    phone = Column(String(10), nullable=False)
    birthday = Column('created_at', DateTime, default=func.now())
    other = Column(String(150), nullable=True)
    bd_soon = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=True)
    user: Mapped["User"] = relationship("User", backref="notes", lazy="joined")


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    refresh_token = Column(String(255), nullable=True)
    avatar = Column(String(255), nullable=True)
    confirmed = Column(Boolean, default=False, nullable=True)
