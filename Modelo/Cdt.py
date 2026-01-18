from sqlalchemy import Column, Integer, ForeignKey, Float, Date, Boolean, String
from base import Base

class Cdt(Base):

    __tablename__ = "cdt"

    id = Column(Integer, primary_key = True)
    id_user = Column(Integer, ForeignKey("Usuarios.id"), 
                     nullable = False)
    fecha_inicio = Column(Date, nullable = False)
    fecha_fin = Column(Date, nullable = False)
    entidad_responsable = Column(String, nullable = False)
    porcentaje_de_rentabilidad = Column(Float, nullable = False)
    renovacion = Column(Boolean, nullable = False)
    porcentaje_invercion_de_rentabilidad = Column(Float, nullable = False)
    id_moneda_transaccion = Column(Integer, ForeignKey("Monedas.id"), 
                                   nullable = False)
    monto_cdt = Column(Float, nullable = False)