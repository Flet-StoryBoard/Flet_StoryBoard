from ..utils.get_system_name import get_system_name
import flet




def set_page_theme (page:flet.Page):
    page.theme_mode = flet.ThemeMode.DARK
    page.padding = 0
    page.spacing = 0
    if get_system_name() == "mac":
        page.bgcolor = flet.colors.TRANSPARENT
        page.window_title_bar_hidden = True
        page.window_title_bar_buttons_hidden = True
        page.window_frameless = True
    else:
        page.bgcolor = flet.colors.BLACK