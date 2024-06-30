



def get_main_key_of_keyboard_event (event_class):
    if event_class.shift: return "shift"
    elif event_class.ctrl: return "ctrl"
    elif event_class.alt: return "alt"
    elif event_class.meta: return "meta"
    else: None