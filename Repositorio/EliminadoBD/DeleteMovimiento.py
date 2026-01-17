from sqlalchemy.orm import Session
from Modelo.Movimientos import Movimientos

def DeleteMovimiento(
    db:Session,
    id_movimiento  
):
    movimientos_db = db.query(Movimientos).filter(
        Movimientos.id == id_movimiento
    ).first()

    db.delete(movimientos_db)
    db.commit()