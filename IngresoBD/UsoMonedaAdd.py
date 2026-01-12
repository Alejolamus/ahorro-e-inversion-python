from Modelo.UsosDeDivisas import UsoDeDivisas
from sqlalchemy.orm import Session
from datetime import date
def CrearUsuario(
        db:Session,
        IdUsuario: int,
        Tipo: str,
        Nombre: str,
        Corte: date,
        IdMoneda: int,
        RegistroAuto: bool,
        Frecuencia: str,
        MontoTransaccion: float
):
    UsoMoney = UsoDeDivisas(
        id_usuario = IdUsuario,
        tipo = Tipo,
        nombre = Nombre,
        creacion = date.today(),
        corte = Corte,
        id_moneda = IdMoneda,
        registro_automatico = RegistroAuto,
        frecuencia = Frecuencia,
        monto_transaccion = MontoTransaccion
    )
    db.add(UsoMoney)
    db.commit()
    db.refresh(UsoMoney)
    return UsoMoney