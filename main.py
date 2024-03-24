from fastapi import Depends, FastAPI, HTTPException, Form
from typing import Annotated
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import SessionLocal, engine

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/users/', response_model=schemas.User)
def create_user(user: Annotated[schemas.User, Depends()], db: Session = Depends(get_db)):
    db_user = crud.create_user(db, user)
    return db_user


