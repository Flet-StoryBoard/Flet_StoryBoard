from ..layer import Layer
import flet


class AlertsHintTooltipLayer (flet.Stack):
    """A custom sub-class of flet.Stack class that built to display Alerts and tooltip-hint"""
    def __init__(self, page: flet.Page) -> None:
        super().__init__()
        self.page = page

        self.tooltip_hint_banner = flet.Container(
            bgcolor="#ffe5b3",
            width=185,
            height=40,
            border_radius=15,
            padding=5
        )
        self.__animation_switcher_of_tooltip_banner = flet.AnimatedSwitcher(
            content=self.tooltip_hint_banner,
            duration=5000,
            animate_opacity=400,
            left=15,
            opacity=0.0,
            transition=flet.AnimatedSwitcherTransition.FADE
        )
        self.controls.append(self.__animation_switcher_of_tooltip_banner)
    

    def show_tooltip_with_content (self, text:str, keyboard_shortcut1:str=None, keyboard_shortcut2:str=None):
        """Show a tooltip hint text and a keyboard shortcut if there was one"""
        r = flet.Row(
            alignment=flet.MainAxisAlignment.CENTER,
            width=self.tooltip_hint_banner.width,
            height=self.tooltip_hint_banner.height,
            spacing=3
        )

        r.controls.append(flet.Text(value=f"{text}   ", color=flet.colors.BLACK, size=14, expand=True, overflow=flet.TextOverflow.ELLIPSIS))

        if keyboard_shortcut1 is not None:
            ks1 = flet.Container(
                content=flet.Text(keyboard_shortcut1, color="white", weight=flet.FontWeight.W_200, size=11),
                bgcolor="black",
                border_radius=18,
                padding=5
            )
            r.controls.append(ks1)
        
        if keyboard_shortcut1 is not None and keyboard_shortcut2 is not None:
            r.controls.append(flet.Text("&", color=flet.colors.BLACK45))
        
        if keyboard_shortcut2 is not None:
            ks2 = flet.Container(
                content=flet.Text(keyboard_shortcut2, color="white", weight=flet.FontWeight.W_200, size=11),
                bgcolor="black",
                border_radius=18,
                padding=5
            )
            r.controls.append(ks2)

        self.tooltip_hint_banner.content = r
        self.tooltip_hint_banner.update()
        self.__animation_switcher_of_tooltip_banner.opacity = 1.0
        self.__animation_switcher_of_tooltip_banner.update()
    

    def hide_tooltip (self):
        self.__animation_switcher_of_tooltip_banner.opacity = 0.0
        self.__animation_switcher_of_tooltip_banner.update()
    

    def update_components_place(self):
        self.__animation_switcher_of_tooltip_banner.left = 7.5
        self.__animation_switcher_of_tooltip_banner.top = self.page.height - int(self.tooltip_hint_banner.height + 20)