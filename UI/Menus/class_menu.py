import npyscreen

from UI.classes_ui import display_all_classes, display_classes_today
from UI.form_enums import Form


class AllClassesForm(npyscreen.ActionForm):
    def create(self):
        classes_string = display_all_classes()
        for class_str in classes_string:
            self.add(npyscreen.TitleFixedText, name=class_str)

    def on_ok(self):
        self.parentApp(Form.MAIN)

    def on_cancel(self):
        self.parentApp.switchForm(Form.MAIN)


class ClassesToday(npyscreen.ActionForm):
    def create(self):
        classes = display_classes_today()
        for class_str in classes:
            self.add(npyscreen.TitleFixedText, name=class_str)
        if not classes:
            self.add(npyscreen.TitleText, name="There are no classes for today!")

    def on_ok(self):
        self.parentApp.switchForm(Form.MAIN)

    def on_cancel(self):
        self.parentApp.switchForm(Form.MAIN)


class PickClass(npyscreen.ActionForm):
    def create(self):
        self.add(
            npyscreen.FixedText, value="Plan Options", editable=False, color="STANDOUT"
        )

        # Post-Plan Options
        self.options = self.add(
            npyscreen.TitleSelectOne,
            name="Options",
            values=["All Classes", "Class by trainer", "Classes today", "Exit"],
            scroll_exit=True,
            max_height=4,
        )

    def on_ok(self):
        choice = self.options.value
        if not choice:
            npyscreen.notify_confirm(
                "Please select an option or press 'Cancel' to go back.",
                title="No Selection",
            )

        selected = choice[0]
        if selected == 0:
            self.parentApp.switchForm(Form.ALL_CLASS)
        elif selected == 1:
            self.parentApp.switchForm(Form.TRAINER)
        elif selected == 2:
            self.parentApp.setNextForm(Form.CLASS_TODAY)
        elif selected == 3:
            self.parentApp.setNextForm(None)

    def on_cancel(self):
        self.parentApp.switchForm(Form.MAIN)
