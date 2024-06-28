from .buttonholder import ButtonHolder
import flet



class SimpleAppBar (flet.Row):
    """
    SimpleAppBar is a UI component that displayed on the top of a page and only display buttons.

    ## Standerd features:
    1. No Title support.
    2. There is a support of back button with options to hide it/show it and to pass a function to
    apply the back.
    3. Built-in navigationsplitview button with ability to hide the button.
    """
    def __init__(self, navigationsplitview) -> None:
        super().__init__()
        self.navigationsplitview = navigationsplitview

        # Row Props
        self.alignment = flet.MainAxisAlignment.START

        # Elements
        self.navigationsplitview_btn = flet.IconButton(
            icon=flet.icons.MENU_ROUNDED,
            on_click=lambda e: self.switch_navigationsplitview_menu()
        )
        self.controls.append(ButtonHolder(
            content=self.navigationsplitview_btn,
            keyboard_shortcut_name="Toggle Menu",
            keyboard_shortcut_key1="CTRL",
            keyboard_shortcut_key2="n"
        ))

        # Spacer
        self.controls.append(flet.Text("", expand=True))

    def switch_navigationsplitview_menu (self):
        if self.navigationsplitview.menu_section_hidden:
            self.navigationsplitview.show_menu()
        else:
            self.navigationsplitview.hide_menu()