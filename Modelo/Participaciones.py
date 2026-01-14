from sqlalchemy import Column, Integer, String, ForeignKey, Float, Enum as SQLEnum, Date
from sqlalchemy.orm import relationship
from enum import Enum
from database import Base


class Inversiones(str, Enum):
    FIC = "FIC"
    INDX = "INDX"
    ETFS = "ETFs"


class Participaciones(Base):
    __tablename__ = "Participaciones"

    id = Column(Integer, primary_key=True)

    id_user = Column(
        Integer,
        ForeignKey("Usuarios.id"),
        nullable=False
    )

    tipo_de_inversion = Column(
        SQLEnum(Inversiones),
        name="inversiones_por_participacion",
        nullable=False
    )

    fecha_de_inicio = Column(Date, nullable=False)
    entidad = Column(String, nullable=False)
    numero_de_participaciones = Column(Integer, nullable=False)
    id_moneda_participacion = Column(Integer, nullable=False)
    valor_participacion = Column(Float, nullable=False)

    registro_inversiones = relationship(
        "RegistroDeParticipaciones",
        cascade="all, delete, delete-orphan"
    )