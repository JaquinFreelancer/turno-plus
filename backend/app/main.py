from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models
from .database import engine
from .deps import get_db
from .schemas import UserCreate  # <-- importar el nuevo schema

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/users/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@app.get("/users/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
