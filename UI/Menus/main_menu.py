import npyscreen


class MainMenu(IMenu):
    def create(self):
        """Create the main menu UI"""
        self.title = self.add(
            npyscreen.FixedText, 
            value="Welcome to City Gym Hub - where we are all about the gains!", 
            editable=False, 
            color="STANDOUT"
        )

        self.user_info = self.add(
            npyscreen.FixedText,
            value="",  # Placeholder for user info
            editable=False, 
            color="STANDOUT"
        )

        # Menu Options
        self.options = self.add(
            npyscreen.TitleSelectOne,
            name="Options",
            values=["View Subscription Plans", "Book A Class", "See Classes", "Exit"],
            scroll_exit=True,
            max_height=6,
        )

    def before_editing(self):
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
        self.display()

    def on_ok(self):
        if self.options.value is not None and len(self.options.value) > 0:
            selected = self.options.value[0]
            if selected == 0:
                self.parentApp.getForm(Form.SUBSCRIPTION).update_subscription()
                self.parentApp.switchForm(Form.SUBSCRIPTION)
            elif selected == 1:
                npyscreen.notify_confirm("Feature coming soon!", title="Book a Class")
                self.parentApp.switchForm(Form.MAIN)
            elif selected == 2:
                self.parentApp.switchForm(Form.PICK_CLASS)
            elif selected == 3:
                self.parentApp.setNextForm(None)
        else:
            npyscreen.notify_confirm(
                "Please select an option to proceed.", title="Error"
            )
            self.parentApp.switchForm(Form.MAIN)

    def on_cancel(self):
        self.parentApp.setNextForm(None)
