from kivy.uix.screenmanager import Screen

class NuevoIngresoScreen(Screen):

    def on_text_change(self):
        ids = self.ids
        self.ids.registro_ingreso.disabled = not (
            ids.nombre_ingreso.text and
            ids.fecha_inicio.text and
            ids.fecha_fin.text and
            ids.tipo_ingreso.text and
            ids.frecuencia.text and
            ids.moneda.text and
            ids.monto.text
        )