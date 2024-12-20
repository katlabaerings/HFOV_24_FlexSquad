import npyscreen

from UI.interfaces.i_menu import IMenu
from UI.form_enums import Form
from Logic.class_logic import ClassLogic


# For the user stories:
# "As a fitness trainer I want to see how many members are attending my class so that I can be better prepared for each class"
class TrainerMenuForm(IMenu):
    def create(self):
        self.classes_status = self.add(
            npyscreen.TitleText, name="Trainer ID: ", color="STANDOUT"
        )

    def fetch_classes(self, trainer_id):
        class_logic = ClassLogic()
        return class_logic.get_classes_by_trainer(trainer_id)

    def on_ok(self):
        trainer_id = self.classes_status.value
        if trainer_id:
            classes = self.fetch_classes(trainer_id)

            self.parentApp.getForm(Form.CLASS_MENU).set_classes(classes)
            npyscreen.notify_confirm(str(classes))
            self.parentApp.switchForm(Form.CLASS_MENU)

    def on_cancel(self):
        self.parentApp.switchForm(Form.MAIN)


class ClassMenuForm(IMenu):
    def create(self):
        self.add(npyscreen.FixedText, value="Classes", editable=False, color="STANDOUT")

        self.class_menu = self.add(
            npyscreen.BoxTitle,
            name="Classes",
            values=[],
            max_height=20,
            rely=2,
        )
        self.class_menu.when_value_edited = self.on_select

    def set_classes(self, classes):
        self.fitness_classes = classes
        self.class_menu.values = [
            f"{cls.class_name} ({cls.current_capacity}/{cls.max_capacity}) - {cls.time} on {cls.date}"
            for cls in self.fitness_classes
        ]
        self.class_menu.display()

    def on_select(self):
        if self.class_menu.value is not None and self.fitness_classes:
            selected_class = self.fitness_classes[self.class_menu.value]
            details = (
                f"Class: {selected_class.class_name}\n"
                f"Trainer: {selected_class.trainer_id.firstname} {selected_class.trainer_id.lastname}\n"
                f"Capacity: {selected_class.current_capacity}/{selected_class.max_capacity}\n"
                f"Time: {selected_class.time}\n"
                f"Date: {selected_class.date}\n"
                f"Locality: {selected_class.locality}\n"
                f"Link: {selected_class.link}"
            )
            npyscreen.notify_confirm(details, title="Fitness Class Details")

    def on_ok(self):
        self.parentApp.switchForm(Form.MAIN)

    def on_cancel(self):
        self.parentApp.switchForm(Form.MAIN)
