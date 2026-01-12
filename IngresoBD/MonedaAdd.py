from Modelo.Monedas import Monedas
from sqlalchemy.orm import Session

def CrearNuevaMoneda(
        db:Session,
        Country: str,
        IsoAL2: str,
        IsoAL3: str,
        NombreDeVivisa: str,
        CodigoDeDivisa: str,
        SimboloDivisa: str    
):
    Money = Monedas(
        pais = Country,
        iso_alpha2 = IsoAL2,
        iso_alpha3 = IsoAL3,
        nombre_divisa = NombreDeVivisa,
        codigo_divisa = CodigoDeDivisa,
        simbolo = SimboloDivisa
    )
    db.add(Money)
    db.commit()
    db.refresh(Money)
    return Money