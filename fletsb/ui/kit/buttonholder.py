import flet, time



class ButtonHolder (flet.Container):
    def __init__(self, content, keyboard_shortcut_name:str="", keyboard_shortcut_key1="", keyboard_shortcut_key2="") -> None:
        super().__init__()
        self.keyboard_shortcut_name = keyboard_shortcut_name
        self.keyboard_shortcut_key1 = keyboard_shortcut_key1
        self.keyboard_shortcut_key2 = keyboard_shortcut_key2

        self.content = content
        self.on_hover = self.on_hover_action

        self.is_still_hovered_at = False

    def on_hover_action (self, e):
        # self.app_class.alerts_and_hinttooltip_layer.
        if self.content.visible == False: return
        is_hover = e.data=="true"

        app_class = self.page.app_class
        if is_hover:
            self.is_still_hovered_at = True
            for i in range(2):
                if self.is_still_hovered_at == False:
                    return
                time.sleep(0.5)
            app_class.alerts_and_hinttooltip_layer.show_tooltip_with_content(
                text=self.keyboard_shortcut_name,
                keyboard_shortcut1=self.keyboard_shortcut_key1,
                keyboard_shortcut2=self.keyboard_shortcut_key2
            )
        else:
            self.is_still_hovered_at = False
            app_class.alerts_and_hinttooltip_layer.hide_tooltip()
    

    def button_function_called_from_shortcut (self):
        app_class = self.page.app_class
        app_class.alerts_and_hinttooltip_layer.hide_tooltip()

        if self.content.visible == False or self.content.page is None:
            # Do not do event if button is not apeared to be existed
            return

        try:
            self.content.on_click()
        except Exception as e:
            print(f"Error while running shortcut '{self.keyboard_shortcut_key1}+{self.keyboard_shortcut_key2}': {e}")


    @property
    def page (self):
        return self.__page
    
    @page.setter
    def page (self, value):
        self.__page = value

        # Give app shortcuts the button function
        if hasattr(self.content, "on_click"):
            if self.content.on_click != None:
                self.__page.app_class.keyboard_shortcuts_with_functions.append(
                    {
                        "main_key": self.keyboard_shortcut_key1,
                        "sub_key": self.keyboard_shortcut_key2,
                        "function": self.button_function_called_from_shortcut
                    }
                )