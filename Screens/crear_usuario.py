from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

class CrearUsuarioScreen(Screen):
    dialog = None
    def on_text_change(self):
        ids = self.ids
        self.ids.boton_registrar.disabled = not (
            ids.username.text and
            ids.correo.text and
            ids.confirmar_correo.text and
            ids.contraseña.text and
            ids.confirmar_contraseña.text
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
    def registrar_usuario(self):
        app = App.get_running_app()

        resultado = app.usuario_controller.crear_usuario(
            self.ids.username.text,
            self.ids.correo.text,
            self.ids.confirmar_correo.text,
            self.ids.contraseña.text,
            self.ids.confirmar_contraseña.text
        )

        self.mostrar_dialogo(resultado)

