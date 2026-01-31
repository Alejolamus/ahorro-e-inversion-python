from Modelo.Movimientos import Movimientos
from sqlalchemy.orm import Session
from datetime import date
def CrearMovimiento(
        db:Session,
        IdUsuario: int,
        IdUsoDiv: int,
        fechamov: date,
        idmoneda: int,
        monto: float
):
    Movimiento = Movimientos(
        id_usuario = IdUsuario,
        id_uso_divisa= IdUsoDiv,
        fecha_movimiento = fechamov,
        id_moneda = idmoneda,
        monto = monto
        
    )
    db.add(Movimiento)
    db.commit()
    db.refresh(Movimiento)
    return Movimiento