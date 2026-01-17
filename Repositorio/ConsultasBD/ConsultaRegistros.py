from sqlalchemy.orm import Session
from Modelo.RegistroDeParticipaciones import RegistroDeParticipaciones

def ConsultaRegistros(
    db:Session,
    id_de_participacion: int ,

):
    registro_db = db.query(RegistroDeParticipaciones).filter(
        RegistroDeParticipaciones.id_participacion == id_de_participacion
    ).all()
    return registro_db