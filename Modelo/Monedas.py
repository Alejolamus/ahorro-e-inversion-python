from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from base import Base

class Monedas(Base):
    __tablename__ = "Monedas"

    id = Column(Integer, primary_key = True)
    pais = Column(String, nullable = False)
    iso_alpha2 = Column(String, nullable = False)
    iso_alpha3 = Column(String, nullable = False)
    nombre_divisa = Column(String, nullable = False)
    codigo_divisa = Column(String, nullable = False)
    simbolo = Column(String, nullable = False)
    monedas_de_uso1 = relationship('MonedasEnUso', cascade='save-update')
    movimientos2 = relationship('Movimientos', cascade='save-update')
    uso_de_divisas = relationship('UsoDeDivisas', cascade='save-update')