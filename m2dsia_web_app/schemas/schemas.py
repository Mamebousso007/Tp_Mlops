from pydantic import BaseModel, EmailStr

class User(BaseModel):
    email: EmailStr
    nom: str
    prenom: str
    classe: str

    class Config:
        orm_mode = True
        from_attributes = True