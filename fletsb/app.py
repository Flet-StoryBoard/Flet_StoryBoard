from .ui.page_theme import set_page_theme
from .ui.layer import Layer
from .ui.static_layers.alerts_hint_tooltip_layer import AlertsHintTooltipLayer

from .utils.get_main_key_keyboard_event import get_main_key_of_keyboard_event

from .pages.home import HomePage
import flet, time, threading


class Application:
    def __init__(self, fletsb_file_path:str) -> None:
        # Project information
        self.fletsb_file_path : str = fletsb_file_path

        # App Data
        self.keyboard_shortcuts_with_functions = [] # {"main_key": (for example)"CTRL", "sub_key": (for example): "F", "function": <function>}
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
        self.page.on_keyboard_event = self.on_keyboard_event

        self.on_page_resize()
        self.page.update()
        self.page.window_center()
    

    def open_settings_sheet (self):
        print("Open settings sheet")
    
    # Events handling

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
    

    def on_keyboard_event (self, e):
        main_key = str(get_main_key_of_keyboard_event(event_class=e)).lower()
        sub_key = str(e.key).lower()

        for ke in self.keyboard_shortcuts_with_functions:
            iterate_main_key = ke['main_key']
            iterate_sub_key = ke['sub_key']
            iterate_function = ke['function']

            if str(iterate_main_key).lower() == main_key and str(iterate_sub_key).lower() == sub_key:
                iterate_function()