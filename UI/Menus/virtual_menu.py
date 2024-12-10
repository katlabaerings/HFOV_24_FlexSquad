import npyscreen
from UI.interfaces.i_menu import IMenu
from UI.form_enums import Form
from Logic.class_logic import ClassLogic

"""
This code is used to implement user story 2, sprint 1:
    As a gym member, I want to be able to attend virtual classes, so I can keep 
    working on my health and well-being, even though I can't physically be there
"""


class VirtualMenu(IMenu):
    def create(self):
        self.classes_status = self.add(
            npyscreen.TitleText, name="Trainer ID: ", color="STANDOUT"
        )

    def fetch_virtual_classes(self):
        class_logic = ClassLogic()
        return class_logic.get_virtual_classes()

    def on_ok(self):
        pass

    def on_cancel(self):
        return super().on_cancel()
