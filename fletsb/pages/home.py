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
            on_click_btn=print
        )
        self.main_column_of_menu_section = flet.Column([
            self.menu_section_appbar
        ])
        self.menu_section.content = self.main_column_of_menu_section

        # Content Section
        self.content_section_appbar = SimpleAppBar(navigationsplitview=self)
        self.main_column_of_content = flet.Column([
            self.content_section_appbar
        ])
        self.content_section.content = self.main_column_of_content