import npyscreen
from UI.interfaces.i_menu import IMenu
from UI.form_enums import Form
from Logic.class_logic import ClassLogic

class MainMenu(IMenu):
    def create(self):
        """Create the main menu UI."""
        self.title = self.add(
            npyscreen.FixedText,
            value="Welcome to City Gym Hub - where we are all about the gains!",
            editable=False,
            color="STANDOUT",
        )

        self.user_info = self.add(
            npyscreen.FixedText,
            value="",  # Placeholder for user info
            editable=False,
            color="STANDOUT",
        )

        self.options = self.add(
            npyscreen.TitleSelectOne,
            name="Options",
            values=["View Subscription Plans", "Book A Class", "See Classes", "Exit"],
            scroll_exit=True,
            max_height=6,
        )
        self.before_editing()

    def before_editing(self):
        """Custom logic for MainMenu before editing."""
        # Call the superclass lifecycle
        # npyscreen.notify_confirm("Debug: before_editing called", title="Debug")

        user_id = 3
        # npyscreen.notify_confirm(f"Debug: userid {user_id}", title="Debug")

        if user_id:
            class_logic = ClassLogic()
            class_within_hour = class_logic.is_class_within_next_hour(user_id)
            if class_within_hour:
                self.user_info.value = f"Coming up: {class_within_hour.class_name} at {class_within_hour.time}!"
            else:
                next_class = class_logic.get_next_class(user_id)
                if next_class:
                    self.user_info.value = f"{next_class.class_name} at {next_class.time} {next_class.date}"
                else:
                    self.user_info.value = f"bla{next_class}"

               # self.user_info.value = f"{next_class.class_name} at {next_class.time} {next_class.date}"
            
             # Add loyalty rewards for the user
            member = class_logic.get_member_by_id(user_id) 
            if member:
                loyalty_points = class_logic.calculate_loyalty_points(member.joined_date)
                rewards = class_logic.get_loyalty_rewards(loyalty_points)
                self.user_info.value = (
                    f"Hi {member.firstname}!\n"
                    f"You have {loyalty_points} loyalty points.\n"
                    f"Your rewards: {rewards}"
                )

        else:
            self.user_info.value = "No User ID found. Please log in."
        
        self.display()  # Refresh the UI

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
