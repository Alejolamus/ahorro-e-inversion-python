from sqlalchemy import Column, Integer, String, ForeignKey,Date
from sqlalchemy.orm import relationship

from database import Base

class Usuarios(Base):
    __tablename__ ="Usuarios"

    id = Column(Integer, primary_key = True)
    usuario=Column(String(50), nullable = False)
    pass_hash=Column(String(200), nullable = False)
    creacion_de_usuario=Column(Date, nullable = False)
    correo = Column(String, nullable = False)
    monedas_de_uso = relationship('MonedasEnUso', 
                                  cascade='all, delete, delete-orphan')
    cdts = relationship('Cdt', 
                        cascade='all, delete, delete-orphan')
    movimientos = relationship('Movimientos', 
                               cascade='all, delete, delete-orphan')
    inversiones = relationship('Participaciones', 
                               cascade='all, delete, delete-orphan')
    uso_de_divisas1 = relationship('UsoDeDivisas', 
                                   cascade='all, delete, delete-orphan')