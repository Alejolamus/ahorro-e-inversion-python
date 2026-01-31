from sqlalchemy.orm import Session
from Modelo.UsosDeDivisas import UsoDeDivisas

def ConsultasUso_Nombre(
    db:Session,
    mov_name: str  
):
    Uso_db = db.query(UsoDeDivisas.id).filter(
        UsoDeDivisas.nombre == mov_name
    ).first()
    return Uso_db