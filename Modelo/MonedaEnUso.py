from sqlalchemy import Column, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship

from DeclarativeBase import Base

class MonedasEnUso(Base):
    __tablename__ = "Moneda_en_uso"

    id = Column(int, primary_key=True)
    idUser = Column(Integer, ForeignKey('Usuarios.id'), nullable = False)
    idMoneda = Column(Integer, ForeignKey('Monedas.id'), nullable = False)
    Monto = Column(Float, nullable = False)