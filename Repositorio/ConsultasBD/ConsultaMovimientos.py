from sqlalchemy.orm import Session
from Modelo.Movimientos import Movimientos

def ConsultasParticipaciones(
    db:Session,
    id_usuario: int  
):
    movimientos_db = db.query(Movimientos).filter(
        Movimientos.id_user == id_usuario
    ).all()
    return movimientos_db