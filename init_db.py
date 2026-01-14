from database import engine, Base
from Modelo.Monedas import Monedas
from Modelo.Cdt import Cdt
from Modelo.MonedaEnUso import MonedasEnUso
from Modelo.Usuarios import Usuarios
from Modelo.Participaciones import Participaciones
from Modelo.RegistroDeParticipaciones import RegistroDeParticipaciones
from Modelo.Movimientos import Movimientos
from Modelo.UsosDeDivisas import UsoDeDivisas

def crear_base():
    Base.metadata.create_all(bind=engine)
    print("Base de datos creada correctamente")

if __name__ == "__main__":
    crear_base()