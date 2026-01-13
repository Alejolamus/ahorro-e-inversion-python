from sqlalchemy.orm import Session
from Modelo.Monedas import Monedas

def ConsultaMonedas(
    db:Session,
):
    monedas_db = db.query(Monedas).all()
    return monedas_db