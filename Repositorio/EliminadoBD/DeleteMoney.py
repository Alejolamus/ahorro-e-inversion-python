from sqlalchemy.orm import Session
from Modelo.Monedas import Monedas

def DeleteMoney(
    db:Session,
    id_moneda  
):
    moneda_db = db.query(Monedas).filter(
        Monedas.id == id_moneda
    ).first()

    db.delete(moneda_db)
    db.commit()
