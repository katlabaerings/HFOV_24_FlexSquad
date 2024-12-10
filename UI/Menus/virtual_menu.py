import npyscreen
from UI.interfaces.i_menu import IMenu
from UI.form_enums import Form
from Logic.class_logic import ClassLogic

"""This is the interface that lets users select what virtual class to attend"""


class VirtualMenu(IMenu):
    def create(self):
        class_logic = ClassLogic()
        all_classes = class_logic.get_virtual_classes()
        self.class_names = [
            f"{cls.class_name} ({cls.current_capacity}/{cls.max_capacity}) - {cls.time} on {cls.date}"
            for cls in all_classes
            if str(self.parentApp.user_id) in cls.members.split()
        ]

        self.class_selector = self.add(
            npyscreen.BoxTitle,
            max_height=10,
            name="Available Classes:",
            values=self.class_names,
            scroll_exit=True,
        )

    # def fetch_virtual_classes_by_id(self, id):
    #     ret_lis = []

    #     npyscreen.notify_confirm(str(all_classes))
    #     for a_class in all_classes:
    #         if id in [int(b_class) for b_class in a_class.members.split()]:
    #             ret_lis.append(a_class)
    #     self.class_names = ret_lis
    #     self.display()

    def on_ok(self):
        self.parentApp.switchForm(Form.MAIN)

    def on_cancel(self):
        return super().on_cancel()
