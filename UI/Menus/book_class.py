import npyscreen

from Logic.class_logic import ClassLogic
from UI.classes_ui import display_available_classes


class BookClassMenu(npyscreen.Form):
    def create(self):
        self.classes = self.add(npyscreen.BoxTitle,
                                name="Classes",
                                values=display_available_classes(),
                                max_height=12,
                                scroll_exit=True)


        self.booked_class = self.add(npyscreen.TitleText, name="Class Booked: ")


    def on_ok(self):
        if self.booked_class.value:
            ClassLogic().add_member_to_class(self.parentApp.user_id, self.booked_class.value)