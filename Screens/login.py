from kivy.uix.screenmanager import Screen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.app import App
class LoginScreen(Screen):
    dialog = None
    def on_text_change(self):
        ids = self.ids
        self.ids.button_login.disabled = not (
            ids.contraseña.text and
            ids.correo.text 
        )

    def validar_login(self):
        app = App.get_running_app()

        resultado = app.login_controller.validar_credenciales(
            self.ids.correo.text,
            self.ids.contraseña.text,
        )

        self.mostrar_dialogo(
            mensaje=resultado["Texto"],
            autorizado=resultado["auth_login"]
        )
    def ir_dashboard(self, *args):
        self.dialog.dismiss()
        self.manager.current = "dashboard"
    def mostrar_dialogo(self, mensaje: str, autorizado: bool = False):
        if self.dialog:
            self.dialog.dismiss()

        if autorizado:
            boton = MDFlatButton(
                text="CONTINUAR",
                on_release=self.ir_dashboard
            )
        else:
            boton = MDFlatButton(
                text="OK",
                on_release=self.cerrar_dialogo
            )

        self.dialog = MDDialog(
            title="Información",
            text=mensaje,
            buttons=[boton]
        )
        self.dialog.open()