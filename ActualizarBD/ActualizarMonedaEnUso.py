from sqlalchemy.orm import Session
from Modelo.MonedaEnUso import MonedasEnUso

def ActualizarMonedaEnUso(
    db: Session,
    id_moneda_en_uso: int,
    new_monto: float
):
    moneda_en_uso_db = db.query(MonedasEnUso).filter(
        MonedasEnUso.id == id_moneda_en_uso
    ).first()

    moneda_en_uso_db.monto = new_monto
    db.commit()
    db.refresh(moneda_en_uso_db)

    return moneda_en_uso_db