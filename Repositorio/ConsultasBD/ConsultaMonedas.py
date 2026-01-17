from sqlalchemy.orm import Session
from Modelo.Monedas import Monedas

def ConsultaMonedas(
    db:Session,
):
    monedas_db = db.query(Monedas).all()
    return monedas_db
def consultarIso2(
    db:Session,
    id_moneda: int  
):
    moneda_db = db.query(Monedas).filter(
        Monedas.id == id_moneda
    ).first()
    iso2=moneda_db.iso_alpha2
    return iso2