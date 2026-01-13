from sqlalchemy.orm import Session
from Modelo.Participaciones import Participaciones
from datetime import date
def ActualizarParticipacion(
    db: Session,
    id_participacion: int,
    new_tipo: str,
    new_entidad: str,
    new_num_partiipacion: int,
    new_id_moneda: int,
    new_value_participacion: float
):
    participacion_db = db.query(Participaciones).filter(
        Participaciones.id == id_participacion
    ).first()

    participacion_db.tipo_de_inversion = new_tipo,
    participacion_db.entidad = new_entidad,
    participacion_db.numero_de_participaciones = new_num_partiipacion,
    participacion_db.id_moneda_participacion = new_id_moneda,
    participacion_db.valor_participacion = new_value_participacion,
    
    db.commit()
    db.refresh(participacion_db)

    return participacion_db