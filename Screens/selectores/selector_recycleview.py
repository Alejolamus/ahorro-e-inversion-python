from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleboxlayout import RecycleBoxLayout

from Screens.selectores.selector_item import SelectorItem

class SelectorRecycleView(RecycleView):

    def __init__(self, items, select_callback, **kwargs):
        super().__init__(**kwargs)

        self.data = [
            {
                "texto": item,
                "callback": select_callback
            }
            for item in items
        ]