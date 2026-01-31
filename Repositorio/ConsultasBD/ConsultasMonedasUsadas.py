from sqlalchemy.orm import Session
from Modelo.MonedaEnUso import MonedasEnUso

def ConsultarMonedasUsadas(
    db:Session,
    id_usuario: int  
):
    monedas_usadas_db = db.query(MonedasEnUso).filter(
        MonedasEnUso.id_user == id_usuario
    ).all()
    return monedas_usadas_db
def ConsultaExitMoney(
    db:Session,
    id_money: int  
):
    moneda_consultada_db = db.query(MonedasEnUso.id, MonedasEnUso.monto).filter(
        MonedasEnUso.id_moneda == id_money
    ).first()
    return moneda_consultada_db