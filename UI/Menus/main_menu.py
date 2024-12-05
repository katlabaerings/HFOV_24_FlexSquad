import npyscreen
from Logic.class_logic import ClassLogic

class MainMenu(npyscreen.ActionForm):
    def create(self):
        # Title
        self.title = self.add(
            npyscreen.FixedText, 
            value="Welcome to City Gym Hub - where we are all about the gains!", 
            editable=False, 
            color=""
        )

        self.user_info = self.add(
            npyscreen.FixedText, 
            value="",  # Placeholder for user info
            editable=False,
            color="STANDOUT"
        )
        self.user_info_class_soon = self.add(
            npyscreen.FixedText, 
            value="",  # Placeholder for user info next class
            editable=False, 
            color="STANDOUT"
        )
        # Menu Options
        self.options = self.add(
            npyscreen.TitleSelectOne,
            name="Options",
            values=[
                "View Subscription Plans",
                "Book A Class",
                "See Classes",
                "Exit"
            ],
            scroll_exit=True,
            max_height=6
        )

    def beforeEditing(self):
        # Dynamically update user info before the form is displayed
        user_id = self.parentApp.user_id
        if user_id:
            # self.user_info.value = f"Your next class (User ID: {user_id} placeholder á eftir að sækja nsæta tíma)"
            # call get_next_class
            class_logic = ClassLogic()
            class_within_hour = class_logic.is_class_within_next_hour(user_id)
            if class_within_hour:
                self.user_info_class_soon.value = f"Coming up: {class_within_hour.class_name} at {class_within_hour.time} !"
            else:
                next_class = class_logic.get_next_class(user_id)
                self.user_info.value = f"{next_class.class_name} at {next_class.time} {next_class.date}"
        else:
            self.user_info.value = "No User ID found. Please log in."
        self.display()  # Refresh the screen to show updated info

    def on_ok(self):
        if self.options.value is not None and len(self.options.value) > 0:
            selected = self.options.value[0]
            if selected == 0:
                self.parentApp.getForm('SUBSCRIPTION').update_subscription()
                self.parentApp.switchForm('SUBSCRIPTION')
            elif selected == 1:
                npyscreen.notify_confirm("Feature coming soon!", title="Book a Class")
                self.parentApp.switchForm('MAIN')
            elif selected == 2:
                self.parentApp.switchForm('PICK_CLASS')
            elif selected == 3:
                self.parentApp.setNextForm(None)
        else:
            npyscreen.notify_confirm("Please select an option to proceed.", title="Error")
            self.parentApp.switchForm('MAIN')

    def on_cancel(self):  # This method is called when "Cancel" is pressed
        self.parentApp.setNextForm(None)
