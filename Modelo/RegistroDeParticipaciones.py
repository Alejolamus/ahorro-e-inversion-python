from sqlalchemy import Column, Integer, ForeignKey, Float, Date
from database import Base

class RegistroDeParticipaciones(Base):
    __tablename__ = "registro_de_participaciones"

    id = Column(Integer, primary_key = True)
    id_participacion = Column(Integer, ForeignKey("Participaciones.id"), nullable = False)
    #uso en dias habiles
    dia_de_registro = Column (Date, nullable = False)
    valor_participacion = Column (Float, nullable = False)