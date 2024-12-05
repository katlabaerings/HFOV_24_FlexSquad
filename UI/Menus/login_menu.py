import npyscreen

from UI.interfaces.i_menu import IMenu
from UI.form_enums import Form


class LoginMenu(IMenu):
    def create(self):
        """Create Login UI"""
        self.add(
            npyscreen.FixedText,
            value="Welcome to City Gym Hub - where we are all about the gains!",
            editable=False,
            color="STANDOUT",
        )

        self.input_field = self.add(npyscreen.TitleText, name="Login with you Id:")

    def on_ok(self):
        user_id = self.input_field.value.strip()
        if not user_id:
            npyscreen.notify_confirm("User ID cannot be empty.", title="Error")
            self.parentApp.switchForm(Form.LOGIN)
            return
        else:
            self.parentApp.user_id = user_id
            self.parentApp.switchForm(Form.MAIN)

    def on_cancel(self):
        self.parentApp.setNextForm(None)
