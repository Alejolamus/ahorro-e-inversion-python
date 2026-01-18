from sqlalchemy import Column, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from base import Base

class MonedasEnUso(Base):
    __tablename__ = "Moneda_en_uso"

    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('Usuarios.id'), nullable = False)
    id_moneda = Column(Integer, ForeignKey('Monedas.id'), nullable = False)
    monto = Column(Float, nullable = False)