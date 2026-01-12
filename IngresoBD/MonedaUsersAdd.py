from Modelo.MonedaEnUso import MonedasEnUso
from sqlalchemy.orm import Session

def CrearMonedaDeUsuario(
        db:Session,
        IdUsuario: int,
        IdMoney: int,
        Cantidad: float
):
    MoneyUse = MonedasEnUso(
        id_user = IdUsuario,
        id_moneda = IdMoney,
        monto = Cantidad
    )
    db.add(MoneyUse)
    db.commit()
    db.refresh(MoneyUse)
    return MoneyUse