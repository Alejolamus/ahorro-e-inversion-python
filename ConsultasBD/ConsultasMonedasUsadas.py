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