from sqlalchemy.orm import Session
from db.connexion import engine, Base
from models.models import User as UserModel
from schemas.schemas import User

# Création de la table une seule fois
Base.metadata.create_all(bind=engine)

def create_user(db: Session, user: User):
    db_user = UserModel(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, email: str):
    return db.query(UserModel).filter(UserModel.email == email).first()

def get_all_users(db: Session):
    return db.query(UserModel).all()