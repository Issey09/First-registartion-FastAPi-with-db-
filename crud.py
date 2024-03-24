import models, schemas
from sqlalchemy.orm import Session



def create_user(db: Session, user: schemas.User):
    db_user = models.User(login=user.login, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

