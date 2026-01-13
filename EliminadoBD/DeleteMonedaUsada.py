from sqlalchemy.orm import Session
from Modelo.MonedaEnUso import MonedasEnUso

def DeleteMonedaUsada(
    db:Session,
    id_moneda_usada  
):
    moneda_usada_db = db.query(MonedasEnUso).filter(
        MonedasEnUso.id == id_moneda_usada
    ).first()

    db.delete(moneda_usada_db)
    db.commit()