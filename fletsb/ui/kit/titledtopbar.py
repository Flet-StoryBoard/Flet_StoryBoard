from .buttonholder import ButtonHolder
import flet



class TitledTopBar (flet.Row):
    """A UI component that placed up of the app to display content like the title, heading text and a single button."""
    def __init__(self, title:str, heading:str, btn_icn, on_click_btn):
        super().__init__()

        self.title_label = flet.Text(title, weight=flet.FontWeight.W_900, size=25, expand=True)
        self.controls.append(self.title_label)

        self.bar_btn = flet.IconButton(
            icon=btn_icn,
            icon_size=23,
            on_click=on_click_btn
        )
        self.controls.append(ButtonHolder(
            content=self.bar_btn,
            keyboard_shortcut_name="Settings",
            keyboard_shortcut_key1="CTRL",
            keyboard_shortcut_key2=","
        ))