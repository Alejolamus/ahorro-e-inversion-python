from sqlalchemy import Column, Integer, ForeignKey, Float, Date, Boolean
from sqlalchemy.orm import relationship
from DeclarativeBase import Base

class Cdt(Base):

    __tablename__ = "cdt"

    id = Column(Integer, primary_kay = True)
    id_user = Column(Integer, ForeignKey("Usuarios.id"), nullable = False)
    fecha_inicio = Column(Date, nullable = False)
    fecha_fin = Column(Date, nullable = False)
    porcentaje_de_rentabilidad = Column(Integer, nullable = False)
    renovacion = Column(Boolean, nullable = False)
    porcentaje_invercion_de_rentabilidad = Column(Integer, nullable = False)