import npyscreen

from Logic.class_logic import ClassLogic


class TrainerMenuForm(npyscreen.ActionForm):  # Changed to ActionForm
    def create(self):
        # Title
        self.add(npyscreen.FixedText, value="Trainer Menu", editable=False, color="STANDOUT")
        self.classes_status = self.add(npyscreen.FixedText, value="", editable=False, color="STANDOUT")

    def beforeEditing(self):
        trainer_id = self.parentApp.user_id
        if not trainer_id:
            self.classes_status.value = "Trainer ID is missing. Please log in again."
            return

        class_logic = ClassLogic()
        classes = class_logic.get_classes_by_trainer(trainer_id)
        if not classes:
            self.classes_status.value = "No classes found for the given Trainer ID."
        else:
            self.classes_status.value = f"{len(classes)} classes found for Trainer ID: {trainer_id}."

        self.display()  

    def on_ok(self):  
        trainer_id = self.parentApp.user_id
        if not trainer_id:
            npyscreen.notify_confirm("Trainer ID cannot be empty.", title="Error")
            self.parentApp.switchForm('MAIN')
            return

        class_logic = ClassLogic()
        classes = class_logic.get_classes_by_trainer(trainer_id)
        if not classes:
            npyscreen.notify_confirm("No classes found for the given Trainer ID.", title="Error")
            self.parentApp.switchForm('MAIN')
            return

        self.parentApp.getForm('CLASS_MENU').set_classes(classes)
        self.parentApp.switchForm('CLASS_MENU')

    def on_cancel(self): 
        self.parentApp.switchForm('MAIN')


class ClassMenuForm(npyscreen.ActionForm):  # Optionally change to ActionForm
    def create(self):
        # Title
        self.add(npyscreen.FixedText, value="Classes", editable=False, color="STANDOUT")

        # Class List
        self.class_menu = self.add(
            npyscreen.MultiLineAction,
            values=[],
            max_height=20,
            rely=2,
            editable=False
        )

    def set_classes(self, classes):
        self.fitness_classes = classes
        self.class_menu.values = [
            f"{cls.class_name} - {cls.time} on {cls.date}" for cls in self.fitness_classes
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
        self.parentApp.switchForm('MAIN')

    def on_cancel(self):
        self.parentApp.switchForm('MAIN')
