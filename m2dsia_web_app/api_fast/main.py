from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from db.connexion import SessionLocal
from db import crud
from schemas.schemas import User
from typing import List

app = FastAPI()

# Dépendance pour la session DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API utilisateur"}

# ➕ Créer un utilisateur
@app.post("/users/", response_model=User)
def create_new_user(user: User, db: Session = Depends(get_db)):
    existing = crud.get_user(db, user.email)
    if existing:
        raise HTTPException(status_code=400, detail="Utilisateur déjà existant")
    return crud.create_user(db, user)

# 📋 Lister tous les utilisateurs
@app.get("/users/", response_model=List[User])
def list_users(db: Session = Depends(get_db)):
    return crud.get_all_users(db)

# 🔍 Récupérer un utilisateur par email
@app.get("/users/{email}", response_model=User)
def get_user(email: str, db: Session = Depends(get_db)):
    user = crud.get_user(db, email)
    if user is None:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    return user

# ✏️ Modifier un utilisateur (PUT)
@app.put("/users/{email}", response_model=User)
def update_user(email: str, updated_user: User, db: Session = Depends(get_db)):
    user = crud.get_user(db, email)
    if not user:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    user.nom = updated_user.nom
    user.prenom = updated_user.prenom
    user.classe = updated_user.classe
    db.commit()
    db.refresh(user)
    return user

# ❌ Supprimer un utilisateur
@app.delete("/users/{email}")
def delete_user(email: str, db: Session = Depends(get_db)):
    user = crud.get_user(db, email)
    if not user:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    db.delete(user)
    db.commit()
    return {"message": "Utilisateur supprimé avec succès"}
