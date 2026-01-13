from sqlalchemy.orm import Session
from Modelo.Movimientos import Movimientos
from datetime import date
def ActualizarMovimientos(
    db: Session,
    id_movimiento: int,
    id_new_uso: int,
    new_fecha: date,
    new_id_moneda: int,
    new_monto: float
):
    movimientos_db = db.query(Movimientos).filter(
        Movimientos.id == id_movimiento
    ).first()

    movimientos_db.id_uso_divisa = id_new_uso,
    movimientos_db.fecha_movimiento = new_fecha,
    movimientos_db.id_moneda = new_id_moneda,
    movimientos_db.monto = new_monto

    db.commit()
    db.refresh(movimientos_db.id_uso_divisa)

    return movimientos_db.id_uso_divisa