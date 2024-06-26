from .ui.page_theme import set_page_theme
import flet


class Application:
    def __init__(self, fletsb_file_path:str) -> None:
        # Project information
        self.fletsb_file_path : str = fletsb_file_path
        flet.app(target=self.app)

    def app (self, page: flet.Page):
        self.page : flet.Page = page

        # Page Style
        page.title = "Flet Storyboard"
        page.window_min_width = 750
        page.window_min_height = 550
        set_page_theme(page=page)
        page.update()

        # Main Content
        self.main_stack = flet.Stack()
        self.page.controls.append(self.main_stack)

        self.app_background = flet.Container(
            bgcolor=flet.colors.BLACK,
            border_radius=18,
            opacity=0.8
        )
        self.main_stack.controls.append(self.app_background)

        self.page.update()
        self.on_page_resize()

        # Set Page Events
        self.page.on_resize = self.on_page_resize
        self.page.update()
    

    def on_page_resize (self, e=None):
        self.app_background.width = self.page.width
        self.app_background.height = self.page.height


        self.page.update()