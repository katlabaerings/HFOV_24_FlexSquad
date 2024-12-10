import npyscreen

from Logic.class_logic import ClassLogic
from UI.classes_ui import display_available_classes
from UI.Menus.main_menu import Form


# This code is for the user story:
# "As a gym member I want to be able to book classes easily through platforms such as an app"
class BookClassMenu(npyscreen.ActionForm):
    def create(self):
        self.classes = self.add(
            npyscreen.BoxTitle,
            name="Classes",
            values=display_available_classes(),
            max_height=12,
            scroll_exit=True,
        )

        self.booked_class = self.add(npyscreen.TitleText, name="Class Booked: ")

        # Bind the selection event to the handler
        self.classes.when_value_edited = self.set_booked_class

    def set_booked_class(self):
        if self.classes.value is not None:
            class_id = self.classes.value + 1
            self.booked_class.value = str(class_id)
        self.display()

    def on_ok(self):
        self.parentApp.user_id
        if self.booked_class.value:
            added = ClassLogic().add_member_to_class(
                self.parentApp.user_id, int(self.booked_class.value)
            )
            npyscreen.notify_confirm(added)

            self.parentApp.switchForm(Form.MAIN)

    def on_cancel(self):
        self.parentApp.switchForm(Form.MAIN)
