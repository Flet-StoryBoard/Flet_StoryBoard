import flet



class NavigationSplitView (flet.Row):
    def __init__ (self):
        super().__init__()
        self.__menu_section_hidden = False
        self.animation_duration = 250

        # Self Row Props
        self.spacing = 0

        # Element
        self.menu_section = flet.Container(
            animate=flet.animation.Animation(duration=self.animation_duration, curve=flet.AnimationCurve.EASE_IN),
            border=flet.border.only(right=flet.BorderSide(width=1, color="#323232")),
            padding=20
        )
        self.controls.append(self.menu_section)

        
        self.content_section = flet.Container(
            animate=flet.animation.Animation(duration=self.animation_duration, curve=flet.AnimationCurve.EASE_IN)
        )
        self.controls.append(self.content_section)
    

    def hide_menu (self):
        self.__menu_section_hidden = True
        self.update_event()

    def show_menu (self):
        self.__menu_section_hidden = False
        self.update_event()
    
    def update_event (self):
        if self.__menu_section_hidden:
            self.menu_section.width = 0
            self.content_section.width = self.width
        else:
            self.menu_section.width = 200
            self.content_section.width = self.width - 200
        
        self.menu_section.height = self.height
        self.content_section.height = self.height

        if self.page is not None:
            self.menu_section.update()
            self.content_section.update()
    

    # props
    @property
    def menu_section_hidden (self):
        return self.__menu_section_hidden