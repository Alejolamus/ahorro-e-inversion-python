from Modelo.Participaciones import Participaciones
from sqlalchemy.orm import Session
from datetime import date
def CrearParticipacion(
        db:Session,
        IdUsuario: int,
        TipoDeInversion: str,
        Entidad: str,
        NumeroParticipaciones: int,
        IdMoneda: int,
        ValorParticipacion: float
):
    Inversion = Participaciones(
        id_user = IdUsuario,
        tipo_de_inversion = TipoDeInversion,
        fecha_de_inicio = date.today(),
        entidad = Entidad,
        numero_de_participacione = NumeroParticipaciones,
        id_moneda_participacion = IdMoneda,
        valor_participacion = ValorParticipacion
    )
    db.add(Inversion)
    db.commit()
    db.refresh(Inversion)
    return Inversion