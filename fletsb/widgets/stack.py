from .row import Row
import flet


class Stack (Row):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.flet_object = flet.Stack()
        self.flet_empty_placeholder_object = flet.Text("Empty Stack")
        self.data['widget_name'] = "Stack"