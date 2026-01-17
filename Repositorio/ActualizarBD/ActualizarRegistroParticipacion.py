from sqlalchemy.orm import Session
from Modelo.RegistroDeParticipaciones import RegistroDeParticipaciones
from datetime import date
def ActualizarRegistroParticipacion(
    db: Session,
    id_registro: int,
    new_id_partiipacion: int,
    new_dia: date,
    new_value: float
 
):
    registro_db = db.query(RegistroDeParticipaciones).filter(
        RegistroDeParticipaciones.id == id_registro
    ).first()

    registro_db.id_participacion = new_id_partiipacion,
    registro_db.dia_de_registro = new_dia,
    registro_db.valor_participacion = new_value

    db.commit()
    db.refresh(registro_db)

    return registro_db