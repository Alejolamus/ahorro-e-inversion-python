from Modelo.Cdt import Cdt
from sqlalchemy.orm import Session
from datetime import date
def CrearParticipacion(
        db:Session,
        IdUsuario: int,
        FechaInicio: date,
        FechaFin: date,
        Entidad: str,
        Rentabilidad: float,
        Renovacion: bool,
        PorcentajeReinvercionRenta: float,
        IdMoneda: int,
        MontoCdt: float
):
    Cdt = Cdt(
        id_user = IdUsuario,
        fecha_inicio = FechaInicio,
        fecha_fin = FechaFin,
        entidad_responsable = Entidad,
        porcentaje_de_rentabilidad = Rentabilidad,
        renovacion = Renovacion,
        porcentaje_invercion_de_rentabilidad = PorcentajeReinvercionRenta,
        id_moneda_transaccion = IdMoneda,
        monto_cdt = MontoCdt
    )
    db.add(Cdt)
    db.commit()
    db.refresh(Cdt)
    return Cdt