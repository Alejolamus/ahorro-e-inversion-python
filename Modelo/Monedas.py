from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from DeclarativeBase import Base

class Monedas(Base):
    __tablename__ = "Monedas"

    id = Column(Integer, primary_key = True)
    Pais = Column(String, nullable = False)
    IsoAlpha2 = Column(String, nullable = False)
    IsoAlpha3 = Column(String, nullable = False)
    NombreDivisa = Column(String, nullable = False)
    CodigoDivisa = Column(String, nullable = False)
    Simbolo = Column(String, nullable = False)
    monedas_de_uso1 = relationship('MonedasEnUso', cascade='save-update')
    movimientos2 = relationship('Movimientos', cascade='save-update')
    uso_de_divisas = relationship('UsoDeDivisas', cascade='save-update')