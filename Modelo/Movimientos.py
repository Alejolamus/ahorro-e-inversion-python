from sqlalchemy import Column, Integer, ForeignKey, Float, Date
from sqlalchemy.orm import relationship

from DeclarativeBase import Base

class Movimientos(Base):
    __tablename__ ="movimientos"

    id = Column(Integer, primary_key = True)
    id_user = Column(Integer, ForeignKey("Usuarios.id"), nullable = False)
    id_uso_divisa = Column(Integer, ForeignKey("Uso_de_divisas.id"), nullable = False)
    fecha_movimiento = Column(Date, nullable=False)
    id_moneda = Column(Integer, ForeignKey("Monedas.id"), nullable = False)
    monto = Column(Float, nullable = False)