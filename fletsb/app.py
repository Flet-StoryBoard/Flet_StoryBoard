from .ui.page_theme import set_page_theme
from .ui.layer import Layer
from .ui.static_layers.alerts_hint_tooltip_layer import AlertsHintTooltipLayer

from .pages.home import HomePage
import flet, time


class Application:
    def __init__(self, fletsb_file_path:str) -> None:
        # Project information
        self.fletsb_file_path : str = fletsb_file_path
        flet.app(target=self.app)

    def app (self, page: flet.Page):
        self.page : flet.Page = page
        self.page.theme = flet.Theme(color_scheme_seed="#5c8fff")
        self.page.app_class = self

        # Page Style
        page.title = "Flet Storyboard"
        page.window_min_width = 750
        page.window_min_height = 550
        set_page_theme(page=page)
        page.update()

        # Main Content
        self.main_stack = flet.Stack()
        self.page.controls.append(self.main_stack)

        #? Background Layer
        self.app_background = flet.Container(
            bgcolor=flet.colors.BLACK,
            border_radius=18,
            opacity=0.8
        )
        self.main_stack.controls.append(self.app_background)

        #? Contents Layer
        self.content_layer = Layer()
        self.content_layer.content = HomePage()
        self.main_stack.controls.append(self.content_layer)

        self.page.update()

        #? Sheets layer

        #? Alerts & hint-tooltip layer
        self.alerts_and_hinttooltip_layer = AlertsHintTooltipLayer(page=self.page)
        self.main_stack.controls.append(self.alerts_and_hinttooltip_layer)

        # Set Page Events
        self.application_layers = [self.content_layer]
        self.page.on_resize = self.on_page_resize
        self.on_page_resize()
        self.page.update()
        self.page.window_center()
    

    def on_page_resize (self, e=None):
        self.app_background.width = self.page.width
        self.app_background.height = self.page.height

        # update layers
        for layer in self.application_layers:
            layer.width = self.page.width
            layer.height = self.page.height
            layer.on_update_function()
        # update Custom layers
        self.alerts_and_hinttooltip_layer.width = self.page.width
        self.alerts_and_hinttooltip_layer.height = self.page.height
        self.alerts_and_hinttooltip_layer.update_components_place()

        self.page.update()