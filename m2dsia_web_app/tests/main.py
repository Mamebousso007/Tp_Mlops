import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from db.connexion import SessionLocal
from schemas.schemas import User
from db.crud import create_user

if __name__ == "__main__":
    db = SessionLocal()

    users_data = [
        {
            "email": "abdoul.fall@isi.com",
            "nom": "Abdoul",
            "prenom": "Fall",
            "classe": "MLOps 2025"
        },
        {
            "email": "diarra.mame@isi.com",
            "nom": "Diarra",
            "prenom": "Mame",
            "classe": "Data Engineer"
        },
        {
            "email": "fall.aminata@isi.com",
            "nom": "Fall",
            "prenom": "Aminata",
            "classe": "Data Analyst"
        },
        {
            "email": "ndour.cheikh@isi.com",
            "nom": "Ndour",
            "prenom": "Cheikh",
            "classe": "MLOps 2025"
        },
        {
            "email": "sy.moussa@isi.com",
            "nom": "Sy",
            "prenom": "Moussa",
            "classe": "DevOps"
        }
    ]

    for data in users_data:
        user = User(**data)
        result = create_user(db, user)
        print(User.model_validate(result).model_dump())

    db.close()
