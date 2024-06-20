from typing import List

from fastapi import APIRouter, HTTPException, Depends, status
from fastapi_limiter.depends import RateLimiter
from sqlalchemy.orm import Session

from src.database.db import get_db
from src.schemas import NoteModel, NoteResponse
from src.database.models import User
from src.repository import notes as repository_notes
from src.services.auth import auth_service

router = APIRouter(prefix="/notes")


@router.post("/", response_model=NoteResponse, dependencies=[Depends(RateLimiter(times=1, seconds=20))])
async def create_note(body: NoteModel, db: Session = Depends(get_db), user: User = Depends(auth_service.get_current_user)):
    return await repository_notes.create_note(body, db, user)


@router.get("/", response_model=List[NoteResponse], dependencies=[Depends(RateLimiter(times=1, seconds=20))])
async def read_notes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), user: User = Depends(auth_service.get_current_user)):
    notes = await repository_notes.get_notes(skip, limit, db, user)
    return notes


@router.get("/{note_id}", response_model=NoteResponse)
async def read_note_id(note_id: int, db: Session = Depends(get_db), user: User = Depends(auth_service.get_current_user)):
    print('1')
    note = await repository_notes.get_note(note_id, db, user)
    if note is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Note not found3"
        )
    return note


@router.put("/{note_id}", response_model=NoteResponse)
async def update_note(body: NoteModel, note_id: int, db: Session = Depends(get_db), user: User = Depends(auth_service.get_current_user)):
    print('q')
    note = await repository_notes.update_note(note_id, body, db, user)
    if note is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Note not found"
        )
    return note


@router.delete("/{note_id}", response_model=NoteResponse)
async def remove_note(note_id: int, db: Session = Depends(get_db), user: User = Depends(auth_service.get_current_user)):
    note = await repository_notes.remove_note(note_id, db, user)
    if note is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Note not found"
        )
    return note

#
@router.get("/name/{note_name}", response_model=NoteResponse)
async def find_note_by_name(note_name: str, db: Session = Depends(get_db), user: User = Depends(auth_service.get_current_user)):
    print('2')
    note = await repository_notes.get_name(note_name, db, user)
    if note is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Note not found"
        )
    return note


@router.get("/familyname/{note_familyname}", response_model=NoteResponse)
async def find_note_by_familyname(note_familyname: str, db: Session = Depends(get_db), user: User = Depends(auth_service.get_current_user)):
    print('3')
    note = await repository_notes.get_familyname(note_familyname, db, user)
    if note is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Note not found"
        )
    return note


@router.get("/email/{note_email}", response_model=NoteResponse)
async def find_note_by_email(note_email: str, db: Session = Depends(get_db), user: User = Depends(auth_service.get_current_user)):
    print('4')
    note = await repository_notes.get_email(note_email, db, user)
    if note is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Note not found"
        )
    return note


@router.get("/k/birthdays", response_model=List[NoteResponse])
async def show_time(db: Session = Depends(get_db), user: User = Depends(auth_service.get_current_user)):
    print('ww')
    notes = await repository_notes.get_birthday(db, user)
    return notes
