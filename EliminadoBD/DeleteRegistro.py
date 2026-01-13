from sqlalchemy.orm import Session
from Modelo.RegistroDeParticipaciones import RegistroDeParticipaciones

def DeleteUser(
    db:Session,
    id_registro  
):
    registro_db = db.query(RegistroDeParticipaciones).filter(
        RegistroDeParticipaciones.id == id_registro
    ).first()

    db.delete(registro_db)
    db.commit()