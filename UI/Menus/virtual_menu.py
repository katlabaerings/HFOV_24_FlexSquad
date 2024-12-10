import npyscreen
import webbrowser
from UI.interfaces.i_menu import IMenu
from Data.read_data import ReadData
from UI.form_enums import Form


class VirtualMenu(IMenu):
    def create(self):
        self.add(npyscreen.FixedText, value="Classes", editable=False, color="STANDOUT")

        self.class_menu = self.add(
            npyscreen.BoxTitle,
            name="Classes",
            values=[],
            max_height=20,
            rely=2,
            scroll_exit=True,
        )
        self.class_menu.when_value_edited = self.on_select

    def set_classes(self):
        self.fitness_classes = ReadData().get_all_classes()
        self.class_menu.values = [
            f"{cls.class_name} ({cls.current_capacity}/{cls.max_capacity}) - {cls.time} on {cls.date}"
            for cls in self.fitness_classes
            if str(self.parentApp.user_id) in cls.members.split()
            and cls.locality == "V"
        ]
        if not self.class_menu.values:
            self.class_menu.values = ["No virtual classes found."]

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
        
            if selected_class.link:
                webbrowser.open(selected_class.link)
            else:
                npyscreen.notify_confirm("No valid link available for this class.", title="Error")
            

    def on_ok(self):
        self.parentApp.switchForm(Form.MAIN)


    def on_cancel(self):
        self.parentApp.setNextForm(None)
