import npyscreen
from UI.form_enums import Form


class LoginMenu(npyscreen.ActionForm):
    def create(self):
        # Title
        self.add(
            npyscreen.FixedText,
            value="Welcome to City Gym Hub - where we are all about the gains!",
            editable=False,
            color="STANDOUT",
        )

        # Trainer ID Input
        self.input_field = self.add(npyscreen.TitleText, name="Login with you Id:")

    def on_ok(self):  # This method is called when "OK" is pressed
        user_id = self.input_field.value.strip()
        if not user_id:
            npyscreen.notify_confirm("User ID cannot be empty.", title="Error")
            self.parentApp.switchForm(Form.LOGIN)
            return
        else:
            self.parentApp.user_id = user_id
            self.parentApp.switchForm(Form.MAIN)

    def on_cancel(self):  # This method is called when "Cancel" is pressed
        self.parentApp.setNextForm(None)
