from kivymd.app import MDApp
from database import engine
from base import Base
from Modelo.Usuarios import Usuarios
from Modelo.Monedas import Monedas
from Modelo.Cdt import Cdt
from Modelo.MonedaEnUso import MonedasEnUso
from Modelo.Participaciones import Participaciones
from Modelo.RegistroDeParticipaciones import RegistroDeParticipaciones
from Modelo.Movimientos import Movimientos
from Modelo.UsosDeDivisas import UsoDeDivisas
from database import SessionLocal
from MainApp.readKV import ReaderKV
from MainApp.ScreensMG import ScreensMG
from Controladores.UserControllers.crear_usuario_controller import UsuarioController
from Controladores.UserControllers.login_controller import LoginController
from Controladores.UserControllers.dashboard.ingresos.nuevo_ingreso import NuevoIngresoController
from bootstrap.monedas_inyeccion import MonedaBootstrap

class MainApp(MDApp):

    def build(self):
        self.title = "Ahorro e Inversión"

        # Crear BD
        Base.metadata.create_all(bind=engine)

        # Crear UNA sesión
        self.db = SessionLocal()

        #bootstrap
        MonedaBootstrap(self.db).ingreso_monedas_basicas()

        # Crear controllers
        self.usuario_controller = UsuarioController(self.db)
        self.login_controller = LoginController(self.db)
        self.nuevo_ingreso_controller = NuevoIngresoController(self.db)

        ReaderKV()

        return ScreensMG()
    
    def change_screen(self, screen_name):
        self.root.current = screen_name