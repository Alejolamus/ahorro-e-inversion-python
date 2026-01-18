from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Enum as SQLEnum,
    Date,
    Boolean,
    Float
)
from sqlalchemy.orm import relationship
from enum import Enum
from base import Base


class Clasificacion(str, Enum):
    ingreso_recurrente = "Ingreso Recurrente"
    ingreso_ocasional = "Ingreso Ocasional"
    gasto_recurrente = "Gasto Recurrente"
    gasto_ocasional = "Gasto Ocasional"


class Frecuencias(str, Enum):
    Mensual = "Mensual"
    Quincenal = "Quincenal"
    Semanal = "Semanal"


class UsoDeDivisas(Base):
    __tablename__ = "Uso_de_divisas"

    id = Column(Integer, primary_key=True)

    id_usuario = Column(
        Integer,
        ForeignKey("Usuarios.id"),
        nullable=False
    )

    tipo = Column(
        SQLEnum(Clasificacion, name="clasificacion_ingresos_gastos"),
        nullable=False
    )

    nombre = Column(String, nullable=False)

    creacion = Column(Date, nullable=False)
    corte = Column(Date)

    id_moneda = Column(
        Integer,
        ForeignKey("Monedas.id"),
        nullable=False
    )

    registro_automatico = Column(Boolean, nullable=False)

    frecuencia = Column(
        SQLEnum(Frecuencias, name="frecuencia_ingresos"),
        nullable=False
    )

    monto_transaccion = Column(Float, nullable=False)

    movimientos1 = relationship(
        "Movimientos",
        cascade="save-update"
    )