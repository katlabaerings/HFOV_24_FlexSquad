import npyscreen

from UI.interfaces.i_menu import IMenu
from Logic.class_logic import ClassLogic
from UI.form_enums import Form

DEFAULT_TRAINER_ID = 1


class TrainerMenuForm(IMenu):
    def create(self):
        self.title = self.add(
            npyscreen.TitleText,
            name="Enter Trainer ID",
            value=str(DEFAULT_TRAINER_ID),
            editable=True,
            color="STANDOUT",
        )
        self.classes_status = self.add(
            npyscreen.FixedText, value="", editable=False, color="STANDOUT"
        )

    def fetch_classes(self, trainer_id):
        class_logic = ClassLogic()
        return class_logic.get_classes_by_trainer(trainer_id)

    def before_editing(self):
        self.title.value = str(DEFAULT_TRAINER_ID)
        trainer_id = int(self.title.value)
        if not trainer_id:
            self.classes_status.value = "Trainer ID is missing. Please log in again."
            return

        classes = self.fetch_classes(trainer_id)
        if not classes:
            self.classes_status.value = "No classes found for the given Trainer ID."
        else:
            self.classes_status.value = f"{len(classes)} classes found, press ok to see details"
        self.display()  

    def on_ok(self):
        trainer_id = int(self.title.value.strip())
        if not trainer_id:
            npyscreen.notify_confirm("Trainer ID cannot be empty.", title="Error")
            self.parentApp.switchForm(Form.MAIN)
            return

        classes = self.fetch_classes(trainer_id)
        if not classes:
            npyscreen.notify_confirm(
                "No classes found for the given Trainer ID.", title="Error"
            )
            self.parentApp.switchForm(Form.MAIN)
            return

        self.parentApp.getForm(Form.CLASS_MENU).set_classes(classes)
        self.parentApp.switchForm(Form.CLASS_MENU)

    def on_cancel(self):
        self.parentApp.switchForm(Form.MAIN)


class ClassMenuForm(IMenu):
    def create(self):
        # Title
        self.add(npyscreen.FixedText, value="Classes", editable=False, color="STANDOUT")

        # Class List
        self.class_menu = self.add(
            npyscreen.MultiLineAction, values=[], max_height=20, rely=2, editable=False
        )

    def set_classes(self, classes):
        self.fitness_classes = classes
        self.class_menu.values = [
            f"{cls.class_name} ({cls.max_capacity}/{cls.current_capacity}) - {cls.time} on {cls.date}" for cls in self.fitness_classes
        ]
        self.class_menu.display()

    def on_select(self, line_value, line_index):  # Corrected method signature
        selected_class = self.fitness_classes[line_index]
        details = (
            f"Class: {selected_class.class_name}\n"
            f"Trainer: {selected_class.trainer.name}\n"
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
