from sqlalchemy.orm import Session
from Modelo.Participaciones import Participaciones

def DeleteParticipacion(
    db:Session,
    id_participacion  
):
    particiion_db = db.query(Participaciones).filter(
        Participaciones.id == id_participacion
    ).first()

    db.delete(particiion_db)
    db.commit()