import flet, threading

class NavigationView (flet.Column):
    def __init__ (self, title:str, on_click_close):
        super().__init__()
        self.scroll = flet.ScrollMode.AUTO

        # Stored-Events data
        self.last_selected = None
        self.all_navigations = {}

        # UI
        self.normal_navigationlink_bgcolor = "#509bff"

        self.back_btn = flet.TextButton(
            text="    Back    ",
            on_click=on_click_close,
            tooltip="Or click Enter or Esc"
        )
        self.controls.append(self.back_btn)

        self.title_label = flet.Text(
            value=f"{title}",
            weight="bold",
            size=35
        )
        self.controls.append(flet.Row([flet.Text(""), self.title_label], spacing=50))


        self.navigations_row = flet.Row([flet.Text("      ")], scroll=flet.ScrollMode.AUTO, spacing=5)
        self.controls.append(self.navigations_row)

        self.content_place = flet.Container()
        self.controls.append(self.content_place)

    

    def add_new_navigation (self, navigation_name:str, navigation_content:flet.Control, on_navigate=None):
        def on_open_navigationpage (e):
            self.open_navigation(navigation_name=navigation_name)
            if on_navigate is not None:
                threading.Thread(target=on_navigate, daemon=True).start()

        label = flet.Text(f"{navigation_name}", color=flet.colors.BLACK)
        c = flet.Container(
            content=flet.Row([
                label
            ], alignment=flet.MainAxisAlignment.CENTER),
            bgcolor="white",
            border_radius=18,
            width=150,
            height=40,
            tooltip=f"Open {navigation_name}"
        )
        self.navigations_row.controls.append(flet.TextButton(content=c, on_click=on_open_navigationpage))

        self.all_navigations[navigation_name] = {
            "content": navigation_content,
            "flet_object": c
        }
    

    def open_navigation (self, navigation_name:str):
        if navigation_name not in self.all_navigations:
            print(f"Error Passed: No navigation named '{navigation_name}'")
            return
        if self.last_selected != None:
            self.last_selected.content.controls[0].color = "black"
            self.last_selected.bgcolor = "white"
            self.last_selected.update()
            
        c = self.all_navigations[navigation_name]['flet_object']
        label = c.content.controls[0]
        self.last_selected = c
        label.color = "white"
        c.bgcolor = "blue"

        self.content_place.content = self.all_navigations[navigation_name]['content']

        if self.content_place.page != None:
            c.update()
            self.back_btn.focus()
            self.content_place.update()


if __name__ == "__main__":
    def test (page:flet.Page):
        page.theme_mode = flet.ThemeMode.DARK
        n = NavigationView("Test", print)
        page.add(n)

        n.add_new_navigation("Home", flet.Text("Home!"))
        n.update()

        n.add_new_navigation("Settings", flet.Text("Settings!"))
        n.update()

        n.add_new_navigation("Community", flet.Text("Communithy!"))
        n.update()
    
    flet.app(target=test)