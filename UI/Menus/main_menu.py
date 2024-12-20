import random
import npyscreen
from UI.interfaces.i_menu import IMenu
from UI.form_enums import Form
from Logic.class_logic import ClassLogic

"""
This code creates the form for the main menu, and user story 7 from sprint 2:
    As a manager I want to see analytics about sign-ups and cancellations so I 
    can take better actions in order to keep them
"""


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

        self.user_loyal = self.add(
            npyscreen.FixedText,
            value="",  # Placeholder for user info
            editable=False,
            color="STANDOUT",
        )

        self.options = self.add(
            npyscreen.TitleSelectOne,
            name="Options",
            values=[
                "View Subscription Plans",
                "Book A Class",
                "See Classes",
                "See Virtual Classes",
                "Exit",
            ],
            scroll_exit=True,
            max_height=6,
        )
        self.options.when_value_edited = self.on_selection_change

    # US9
    def beforeEditing(self):
        """Returns next classes, if it  is within the next hour, and member's loyalty points"""
        # Call the superclass lifecycle
        self.user_id = self.parentApp.user_id
        motivatingList = [
            "We are what we repeatedly do. Excellence, then, is not an act, but a habit.",
            "Just believe in yourself. Even if you don’t, just pretend that you do and at some point, you will.",
            " All progress takes place outside the comfort zone.",
            " Once you are exercising regularly, the hardest thing is to stop it.",
            "Push harder than yesterday if you want a different tomorrow. ",
            "The real workout starts when you want to stop.",
        ]

        randomMotivation = random.choice(motivatingList)

        if self.user_id:
            class_logic = ClassLogic()
            class_within_hour = class_logic.is_class_within_next_hour(self.user_id)
            if class_within_hour:
                # Within the next hour
                self.user_info.value = f"Coming up: {class_within_hour.class_name} at {class_within_hour.time}!\n"
            else:
                # next class
                next_class = class_logic.get_next_class(self.user_id)
                if next_class:
                    self.user_info.value = f"{next_class.class_name} at {next_class.time} {next_class.date}\n"
                else:
                    # Motivaiting out members if they have no classes
                    self.user_info.value = f"{randomMotivation}\n"

            # Add loyalty rewards for the user
            member = class_logic.get_member_by_id(self.user_id)
            if member:
                loyalty_points = class_logic.calculate_loyalty_points(
                    member.joined_date
                )
                rewards = class_logic.get_loyalty_rewards(loyalty_points)
                self.user_loyal.value = (
                    f"Hi {member.firstname}!\n"
                    f"You have {loyalty_points} loyalty points.\n"
                    f"Your rewards: {rewards}"
                )

        else:
            self.user_info.value = "No User ID found. Please log in."
        self.display()  # Refresh the UI

    def on_selection_change(self):
        if self.options.value is not None and len(self.options.value) > 0:
            selected = self.options.value[0]
            match selected:
                case 0:
                    self.parentApp.getForm(Form.SUBSCRIPTION).update_subscription()
                    self.parentApp.switchForm(Form.SUBSCRIPTION)
                case 1:
                    self.parentApp.switchForm(Form.BOOK_CLASS)
                case 2:
                    self.parentApp.switchForm(Form.PICK_CLASS)
                case 3:
                    self.parentApp.switchForm(Form.VIRTUAL_CLASS)
                case 4:
                    self.parentApp.setNextForm(None)

    def on_ok(self):
        self.on_selection_change()

    def on_cancel(self):
        self.parentApp.setNextForm(None)
