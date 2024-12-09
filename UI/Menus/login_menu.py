import npyscreen

from UI.interfaces.i_menu import IMenu
from UI.form_enums import Form
from Logic.class_logic import ClassLogic


class LoginMenu(IMenu):
    def create(self):
        """Create Login UI"""
        self.add(
            npyscreen.FixedText,
            value="Welcome to City Gym Hub - where we are all about the gains!",
            editable=False,
            color="STANDOUT",
        )

        self.input_field = self.add(
            npyscreen.TitleText, name="Login with you Id:", color="STANDOUT"
        )

    def on_ok(self):
        user_id = self.input_field.value.strip()
        if not user_id:
            npyscreen.notify_confirm("User ID cannot be empty.", title="Error")
            self.parentApp.switchForm(Form.LOGIN)
            return
        else:
            self.parentApp.user_id = user_id
            class_logic = ClassLogic()
            classes = class_logic.get_classes_by_trainer(user_id)
            npyscreen.notify_confirm(str(classes))
            self.parentApp.getForm(Form.CLASS_MENU).set_classes(classes)
            self.parentApp.switchForm(Form.MAIN)

    def on_cancel(self):
        self.parentApp.setNextForm(None)
