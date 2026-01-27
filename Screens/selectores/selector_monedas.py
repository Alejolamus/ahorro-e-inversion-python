from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton
from Screens.selectores.selector_recycleview import SelectorRecycleView

class MonedaSelector:

    def __init__(self, get_items_callback, on_select_callback):
        self.get_items_callback = get_items_callback
        self.on_select_callback = on_select_callback
        self.dialog = None

    def open(self):
        items = self.get_items_callback()

        rv = SelectorRecycleView(
            items=items,
            select_callback=self._on_select,
            size_hint_y=None,
            height=300
        )

        content = MDBoxLayout(
        orientation="vertical",
        size_hint_y=None,
        height=350,
        padding=10
    )
        content.add_widget(rv)

        self.dialog = MDDialog(
            title="Seleccionar moneda",
            type="custom",
            content_cls=content,
            buttons=[
                MDFlatButton(
                    text="CANCELAR",
                    on_release=lambda x: self.dialog.dismiss()
                )
            ]
        )

        self.dialog.open()

    def _on_select(self, value):
        self.on_select_callback(value)
        if self.dialog:
            self.dialog.dismiss()
