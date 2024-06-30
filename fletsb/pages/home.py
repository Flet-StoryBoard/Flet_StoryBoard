from ..ui.kit import *
import flet, os

class HomePage (NavigationSplitView):
    def __init__(self) -> None:
        super().__init__()

        # Menu Secrtion
        self.menu_section_appbar = TitledTopBar(
            title="Fletsb",
            heading="my project",
            btn_icn=flet.icons.SETTINGS_ROUNDED,
            on_click_btn=self.open_settings_sheet
        )
        self.main_column_of_menu_section = flet.Column([
            WindowTrafficButtons(),
            self.menu_section_appbar
        ])
        self.menu_section.content = self.main_column_of_menu_section

        # Content Section
        self.content_section_appbar = SimpleAppBar(navigationsplitview=self)
        self.main_column_of_content = flet.Column([
            flet.WindowDragArea(content=self.content_section_appbar)
        ])
        self.content_section.content = self.main_column_of_content
    
    def open_settings_sheet (self, e=None):
        self.page.app_class.open_settings_sheet()