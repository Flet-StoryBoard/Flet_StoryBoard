from .buttonholder import ButtonHolder
import flet, sys



class WindowTrafficButtons (flet.Row):
    """WindowTrafficButtons is a UI component that presents a fullscreen window button and a minimize button"""
    def __init__(self) -> None:
        super().__init__()

        # Close window button
        self.close_window_btn = flet.Container(
            width=15,
            height=15,
            bgcolor="#FF2400",
            border_radius=18,
            on_click=self.exit_app
        )
        self.controls.append(ButtonHolder(
            content=self.close_window_btn,
            keyboard_shortcut_name="Exit app",
            keyboard_shortcut_key1="CTRL",
            keyboard_shortcut_key2="Q"
        ))

        # Minimize window button
        self.minimize_window_btn = flet.Container(
            width=15,
            height=15,
            bgcolor="#FDDA0D",
            border_radius=18,
            on_click=self.minimize_window_screen
        )
        self.controls.append(ButtonHolder(
            content=self.minimize_window_btn,
            keyboard_shortcut_name="Minimize",
            keyboard_shortcut_key1="CTRL",
            keyboard_shortcut_key2="M"
        ))

        # Fullscreen button
        self.fullscreen_btn = flet.Container(
            width=15,
            height=15,
            bgcolor="#7cb46b",
            border_radius=18,
            on_click=self.fullscreen_toggle
        )
        self.controls.append(ButtonHolder(
            content=self.fullscreen_btn,
            keyboard_shortcut_name="Fullscreen",
            keyboard_shortcut_key1="CTRL",
            keyboard_shortcut_key2="F"
        ))
    
    def exit_app (self, e=None):
        self.page.window_close()
    
    
    def fullscreen_toggle (self, e=None):
        if self.page.window_full_screen:
            self.fullscreen_btn.parent.keyboard_shortcut_name = "FullScreen"
            self.minimize_window_btn.visible = True
            self.page.window_full_screen = False
        else:
            self.fullscreen_btn.parent.keyboard_shortcut_name = "Exit FullScreen"
            self.minimize_window_btn.visible = False
            self.page.window_full_screen = True
        
        self.page.update()
    

    def minimize_window_screen (self, e=None):
        if self.page.window_minimized:
            self.page.window_minimized = False
        else:
            self.page.window_minimized = True
        self.page.update()