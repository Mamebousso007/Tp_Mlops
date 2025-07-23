from sqlalchemy import Column, String
from db.connexion import Base

class User(Base):
    __tablename__ = "users"
    email = Column(String(255), primary_key=True, index=True, unique=True, nullable=False)
    nom = Column(String(255), nullable=False)
    prenom = Column(String(255), nullable=False)
    classe = Column(String(255), nullable=False)