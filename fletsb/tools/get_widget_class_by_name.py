from fletsb import widgets


def get_all_widgets ():
    return {
        "Title": "TITLE_ROUNDED",
        "Row": "VIEW_COLUMN_ROUNDED",
        "Column": "TABLE_ROWS_ROUNDED",
        "Stack": "BORDER_HORIZONTAL_SHARP",
        "Paragraph": "SHORT_TEXT_ROUNDED",
        "Image": "IMAGE_OUTLINED",
        "RouteButton": "ROUTE_OUTLINED",
        "TextButton": "SMART_BUTTON_ROUNDED",
        "TextField": "INPUT_ROUNDED",
        "ElevatedButton": "NINETEEN_MP_ROUNDED"
    }


def get_widget_class_by_name (widget_name:str) -> widgets.Widget:
    ws = {
        "Title": widgets.Title,
        "Row": widgets.Row,
        "Column": widgets.Column,
        "Paragraph": widgets.Paragraph,
        "Image": widgets.Image,
        "RouteButton": widgets.RouteButton,
        "TextButton": widgets.TextButton,
        "TextField": widgets.TextField,
        "Stack": widgets.Stack,
        "ElevatedButton": widgets.ElevatedButton
    }


    if widget_name in ws:
        return ws[widget_name]
    else:
        raise Exception(f"Error: No supported widget named '{widget_name}'.")