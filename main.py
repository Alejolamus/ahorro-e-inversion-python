from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from database import engine, Base
from Modelo.Usuarios import Usuarios
from Modelo.Monedas import Monedas
from Modelo.Cdt import Cdt
from Modelo.MonedaEnUso import MonedasEnUso
from Modelo.Participaciones import Participaciones
from Modelo.RegistroDeParticipaciones import RegistroDeParticipaciones
from Modelo.Movimientos import Movimientos
from Modelo.UsosDeDivisas import UsoDeDivisas
from Screens.login import LoginScreen
from Screens.recuperar_password import RecuperarPasswordScreen
from Screens.crear_usuario import CrearUsuarioScreen
from Screens.dashborad import DashboardScreen

class MainApp(MDApp):

    def build(self):
        self.title = "Ahorro e Inversión"

        # Crear BD si no existe (seguro)
        Base.metadata.create_all(bind=engine)

        # Cargar archivos KV
        Builder.load_file("Vista/login.kv")
        Builder.load_file("Vista/crear_usuario.kv")
        Builder.load_file("Vista/recuperar_password.kv")

        # ScreenManager
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name="login_app"))
        sm.add_widget(CrearUsuarioScreen(name="crear_usuario"))
        sm.add_widget(RecuperarPasswordScreen(name="recuperar_password"))
        sm.add_widget(DashboardScreen(name="dashboard"))

        return sm

    def change_screen(self, screen_name):
        self.root.current = screen_name


if __name__ == "__main__":
    MainApp().run()
