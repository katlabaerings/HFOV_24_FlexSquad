import npyscreen

from UI.interfaces.i_menu import IMenu
from UI.classes_ui import display_all_classes, display_classes_today
from UI.form_enums import Form

"""
This code is used to implement user story 1, sprint 1:
    As a gym member I want to be able to see available classes so i can plan 
    what class i want to attend
"""


class AllClassesMenu(IMenu):
    def create(self):
        classes_string = display_all_classes()
        for class_str in classes_string:
            self.add(npyscreen.TitleFixedText, name=class_str)

    def on_ok(self):
        self.parentApp.switchForm(Form.MAIN)

    def on_cancel(self):
        self.parentApp.switchForm(Form.MAIN)


class ClassesTodayMenu(IMenu):
    def create(self):
        classes = display_classes_today()
        for class_str in classes:
            self.add(npyscreen.TitleFixedText, name=class_str)
        if not classes:
            self.add(npyscreen.TitleText, name="There are no classes for today!")
            return

    def on_ok(self):
        self.parentApp.switchForm(Form.MAIN)

    def on_cancel(self):
        self.parentApp.switchForm(Form.MAIN)


class PickClassMenu(IMenu):
    def create(self):
        self.add(npyscreen.FixedText, editable=False, color="STANDOUT")

        # Post-Plan Options
        self.options = self.add(
            npyscreen.TitleSelectOne,
            name="Options",
            values=["All Classes", "Class by trainer", "Classes today", "Exit"],
            scroll_exit=True,
            max_height=4,
        )
        self.options.when_value_edited = self.on_selection_change

    def on_selection_change(self):
        choice = self.options.value

        if choice is not None and len(choice) > 0:
            selected = choice[0]
            match selected:
                case 0:
                    self.parentApp.switchForm(Form.ALL_CLASS)
                case 1:
                    self.parentApp.switchForm(Form.CLASS_MENU)
                case 2:
                    self.parentApp.switchForm(Form.CLASS_TODAY)
                case _:
                    self.parentApp.setNextForm(None)

    def on_ok(self):
        self.on_selection_change()

    def on_cancel(self):
        self.parentApp.switchForm(Form.MAIN)
