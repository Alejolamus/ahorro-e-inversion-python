from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.boxlayout import MDBoxLayout
from Screens.selectores.selector_recycleview import SelectorRecycleView

class SelectorDialog:

    def __init__(self, title, items, on_select, height=300):
        self.on_select = on_select

        rv = SelectorRecycleView(size_hint_y=None, height=height)
        rv.data = [
            {"text": item, "callback": self._select}
            for item in items
        ]

        content = MDBoxLayout(orientation="vertical", padding=10)
        content.add_widget(rv)

        self.dialog = MDDialog(
            title=title,
            type="custom",
            content_cls=content,
            buttons=[
                MDFlatButton(
                    text="CANCELAR",
                    on_release=lambda x: self.dialog.dismiss()
                )
            ]
        )

    def _select(self, value):
        self.on_select(value)
        self.dialog.dismiss()

    def open(self):
        self.dialog.open()
