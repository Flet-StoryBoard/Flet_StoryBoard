import flet



class Layer (flet.Container):
    def __init__(self, fit_content=True) -> None:
        self.fit_content = fit_content
        super().__init__()
    
    def on_update_function (self):
        if self.content is not None:
            if self.fit_content: 
                self.content.width = self.width
                self.content.height = self.height
            if hasattr(self.content, "update_event"):
                self.content.update_event()