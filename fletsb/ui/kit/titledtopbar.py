import flet



class TitledTopBar (flet.Row):
    """A UI component that placed up of the app to display content like the title, heading text and a single button."""
    def __init__(self, title:str, heading:str, btn_icn, on_click_btn):
        super().__init__()

        self.title_label = flet.Text(title, weight=flet.FontWeight.W_900, size=25)
        self.controls.append(self.title_label)