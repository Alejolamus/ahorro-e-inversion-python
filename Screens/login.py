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
    def cerrar_dialogo(self, *args):
        if self.dialog:
            self.dialog.dismiss()
    def mostrar_dialogo(self, mensaje: str):
        # Si hay un diálogo abierto, cerrarlo
        if self.dialog:
            self.dialog.dismiss()

        self.dialog = MDDialog(
            title="Información",
            text=mensaje,
            buttons=[
                MDFlatButton(
                    text="OK",
                    on_release=self.cerrar_dialogo
                )
            ]
        )
        self.dialog.open()

    def validar_login(self):
        app = App.get_running_app()

        resultado = app.login_controller.validar_credenciales(
            self.ids.correo.text,
            self.ids.contraseña.text,
        )

        self.mostrar_dialogo(resultado)
