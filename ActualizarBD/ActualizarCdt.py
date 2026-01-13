from sqlalchemy.orm import Session
from Modelo.Cdt import Cdt
from datetime import date
def ActualizarCdt(
    db: Session,
    id_cdt: int,
    new_fecha_inicio: date,
    new_fecha_fin: date,
    new_entiad: str,
    new_renta: float,
    new_reovacion: bool,
    new_porecntaje_re_inv: float,
    new_id_moneda: int,
    new_monto: float
):
    cdt_db = db.query(Cdt).filter(
        Cdt.id == id_cdt
    ).first()

    cdt_db.fecha_inicio = new_fecha_inicio,
    cdt_db.fecha_fin = new_fecha_fin,
    cdt_db.entidad_responsable = new_entiad,
    cdt_db.porcentaje_de_rentabilidad = new_renta,
    cdt_db.renovacion = new_reovacion,
    cdt_db.porcentaje_invercion_de_rentabilidad = new_porecntaje_re_inv,
    cdt_db.id_moneda_transaccion = new_id_moneda,
    cdt_db.monto_cdt = new_monto
    db.commit()
    db.refresh(cdt_db)

    return cdt_db