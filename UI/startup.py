#!/usr/bin/env python
# encoding: utf-8

import npyscreen


class StartupApp(npyscreen.NPSApp):
    def main(self):
        # These lines create the form and populate it with widgets.
        # A fairly complex screen in only 8 or so lines of code - a line for each control.
        F = npyscreen.Form(
            name="Welcome to City Gym Hub",
        )
        t = F.add(
            npyscreen.TitleText,
            name="Text:",
        )
        dt = F.add(npyscreen.TitleDateCombo, allowPastDate=False, name="Date:")
        s = F.add(npyscreen.TitleSlider, out_of=12, name="Slider")
        ml = F.add(
            npyscreen.MultiLineEdit,
            value="""try typing here!\nMultiline text, press ^R to reformat.\n""",
            max_height=5,
            rely=9,
        )
        ms = F.add(
            npyscreen.TitleSelectOne,
            max_height=4,
            value=[
                1,
            ],
            name="Pick One",
            values=["Book Class", "Subscription Plans"],
            scroll_exit=True,
        )

        # This lets the user interact with the Form.
        F.edit()

        print(ms.get_selected_objects())


if __name__ == "__main__":
    App = StartupApp()
    App.run()
