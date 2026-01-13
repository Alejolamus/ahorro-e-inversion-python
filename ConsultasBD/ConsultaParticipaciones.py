from sqlalchemy.orm import Session
from Modelo.Participaciones import Participaciones

def ConsultasParticipaciones(
    db:Session,
    id_usuario: int  
):
    particiiones_db = db.query(Participaciones).filter(
        Participaciones.id_user == id_usuario
    ).all()
    return particiiones_db