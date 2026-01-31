from Modelo.UsosDeDivisas import UsoDeDivisas, Frecuencias, Clasificacion
from sqlalchemy.orm import Session
from datetime import date
def usomoneda(
        db:Session,
        IdUsuario: int,
        Tipo: Clasificacion,
        Nombre: str,
        Creacion: date,
        Corte: date,
        IdMoneda: int,
        RegistroAuto: bool,
        Frecuencia: Frecuencias
):
    UsoMoney = UsoDeDivisas(
        id_usuario = IdUsuario,
        tipo = Tipo,
        nombre = Nombre,
        creacion = Creacion,
        corte = Corte,
        id_moneda = IdMoneda,
        registro_automatico = RegistroAuto,
        frecuencia = Frecuencia
    )
    db.add(UsoMoney)
    db.commit()
    db.refresh(UsoMoney)
    return UsoMoney