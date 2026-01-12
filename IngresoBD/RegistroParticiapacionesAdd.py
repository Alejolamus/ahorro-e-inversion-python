from Modelo.RegistroDeParticipaciones import RegistroDeParticipaciones
from sqlalchemy.orm import Session
from datetime import date
def CrearUsuario(
        db:Session,
        IdParticipacion: int,
        ValueParticipacion: float
):
    CambioDeValor = RegistroDeParticipaciones(
        id_participacion = IdParticipacion,
        dia_de_registro = date.today(),
        valor_participacion = ValueParticipacion 
    )
    db.add(CambioDeValor)
    db.commit()
    db.refresh(CambioDeValor)
    return CambioDeValor