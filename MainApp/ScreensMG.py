from kivy.uix.screenmanager import ScreenManager
from Screens.recuperar_password import RecuperarPasswordScreen
from Screens.crear_usuario import CrearUsuarioScreen
from Screens.dashboard import DashboardScreen
from Screens.ingresos.interfas_ingresos import InterfasIngresosScreen    
from Screens.login import LoginScreen
from Screens.ingresos.funciones_ingresos.nuevo_ingreso import NuevoIngresoScreen


def ScreensMG(nuevo_ingreso_controller):

    sm = ScreenManager()

    sm.add_widget(LoginScreen(name="login"))
    sm.add_widget(CrearUsuarioScreen(name="crear_usuario"))
    sm.add_widget(RecuperarPasswordScreen(name="recuperar_password"))
    sm.add_widget(DashboardScreen(name="dashboard"))
    sm.add_widget(InterfasIngresosScreen(name="interfas_ingresos"))

    sm.add_widget(
        NuevoIngresoScreen(
            name="nuevo_ingreso",
            controller=nuevo_ingreso_controller
        )
    )

    return sm