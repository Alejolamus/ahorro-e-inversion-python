from kivymd.uix.screen import MDScreen
from Screens.selectores.selector_monedas import MonedaSelector

class NuevoIngresoScreen(MDScreen):

    def __init__(self, controller, **kwargs):
        super().__init__(**kwargs)
        self.controller = controller

        self.moneda_selector = MonedaSelector(
            get_items_callback=self.obtener_monedas,
            on_select_callback=self.moneda_seleccionada
        )
    def obtener_monedas(self):
        return [
            f"{pais} - {divisa}"
            for pais, divisa in self.controller.LlamarMonedasEnBase()
        ]
    def abrir_selector(self):
        self.moneda_selector.open()

    def moneda_seleccionada(self, texto):
        self.ids.moneda_seleccionada.text = texto

