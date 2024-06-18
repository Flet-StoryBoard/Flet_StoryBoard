from .widget import Widget
from .. import utils
import flet



class TextField (Widget):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.flet_object = flet.TextField(
            value="",
            on_focus=lambda e: self.on_textfield_events(event_name="on_focus"),
            on_change=lambda e: self.on_textfield_events(event_name="on_change"),
            on_submit=lambda e: self.on_textfield_events(event_name="on_submit")
        )
        self.data['widget_name'] = "TextField"
        self.availble_events = ["on_change", "on_submit", "on_focus"]

        for ae in self.availble_events:
            self.data['events'][f'{ae}'] = None
    
    def on_textfield_events (self, event_name:str):
        if self.storyboard_class.development_mode:
            pass
        else:
            self.data['value'] = str(self.flet_object.value)
            if not event_name in self.data['events']: return

            function_name_of_event = self.data['events'][event_name]
            if function_name_of_event == None: return

            if function_name_of_event in self.storyboard_class.defined_functions:
                init_the_event_class = utils.EventClass(
                    event_name=event_name,
                    event_data=str(self.flet_object.value),
                    widget_id=self.data['id'],
                    storyboard_class=self.storyboard_class
                )
                self.storyboard_class.defined_functions[function_name_of_event](init_the_event_class)
    
    def update_flet_object(self):
        super().update_flet_object()

        properties = self.data['properties']
        value = properties['value']
        label = properties['label']
        hint_text = properties['hint_text']
        tooltip = properties['tooltip']

        bgcolor = properties['bgcolor']
        color = properties['color']

        resizeable = properties['resizeable']

        width = properties['width']
        height = properties['height']

        self.flet_object.value = str(value)
        self.flet_object.label = str(label)
        self.flet_object.hint_text = str(hint_text)
        self.flet_object.tooltip = str(tooltip)

        self.flet_object.bgcolor = str(bgcolor)
        self.flet_object.color = str(color)
        
        if resizeable:
            self.flet_object.width = width
            self.flet_object.height = height
        else:
            self.flet_object.width = None
            self.flet_object.height = None

        if self.flet_object.page != None:
            self.flet_object.update()
    

    def properties_data(self):
        return {
            "value" : {"type":"str", "default_value":""},
            "label": {"type":"str", "default_value":""},
            "hint_text": {"type":"str", "default_value":"Type.."},
            "tooltip" : {"type":"str", "default_value":""},

            "bgcolor": {"type": "color", "default_value": ""},
            "color": {"type": "color", "default_value": "white"},

            "resizeable": {"type": "bool", "default_value": False},

            "width": {"type": "int", "default_value": 200},
            "height": {"type": "int", "default_value": 50}
        }