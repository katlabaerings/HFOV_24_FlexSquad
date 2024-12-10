import npyscreen

from UI.interfaces.i_menu import IMenu
from Logic.subscription_logic import get_subscription_plans, get_plan_details
from UI.form_enums import Form

"""
This code is used to implement user story 3, sprint 1:
    As a gym member I want more flexible subscription plans, such as one month 
    or a single class, so that I can easily find the best subscription that 
    suits me
"""


class SubscriptionMenu(IMenu):
    def create(self):
        self.add(
            npyscreen.FixedText,
            editable=False,
            color="STANDOUT",
        )

        self.plan_options = self.add(
            npyscreen.TitleSelectOne,
            name="Available Plans",
            values=[],
            scroll_exit=True,
            max_height=10,
        )
        self.plan_options.when_value_edited = self.on_selection_change

    def update_subscription(self):
        plans = get_subscription_plans()
        self.plan_options.values = [plan["PlanName"] for plan in plans]
        self.plan_options.display()

    def on_selection_change(self):
        choice = self.plan_options.value
        if choice is not None and len(choice) > 0:
            selected_plan = self.plan_options.values[choice[0]]
            details = get_plan_details(selected_plan)
            npyscreen.notify_confirm(details, title=f"Plan Details: {selected_plan}")

            if selected_plan == "Class Bundle":
                self.parentApp.getForm(Form.CLASS_BUNDLE).update_bundle_options()
                self.parentApp.switchForm(Form.CLASS_BUNDLE)
            else:
                self.parentApp.getForm(Form.POST_PLAN).selected_plan = selected_plan
                self.parentApp.switchForm(Form.POST_PLAN)

    def on_ok(self):
        self.on_selection_change()

    def on_cancel(self):
        self.parentApp.switchForm(Form.MAIN)


class PostPlanOptionsMenu(IMenu):
    selected_plan = None

    def create(self):
        self.add(
            npyscreen.FixedText, value="Plan Options", editable=False, color="STANDOUT"
        )

        self.options = self.add(
            npyscreen.TitleSelectOne,
            name="Options",
            values=["Buy Plan", "Back to Plans", "Exit"],
            scroll_exit=True,
            max_height=4,
        )

    def on_ok(self):
        choice = self.options.value
        if not choice:
            npyscreen.notify_confirm(
                "Please select an option or press 'Back' to go back.",
                title="No Selection",
            )
            self.parentApp.switchForm(Form.POST_PLAN)
            return
        selected = choice[0]
        if selected == 0:
            npyscreen.notify_confirm(
                f"Thank you for choosing to buy the {self.selected_plan}!",
                title="Purchase Successful",
            )
            self.parentApp.switchForm(Form.MAIN)
        elif selected == 1:
            self.parentApp.switchForm(Form.SUBSCRIPTION)
        elif selected == 2:
            self.parentApp.setNextForm(None)

    def on_cancel(self):
        self.parentApp.switchForm(Form.SUBSCRIPTION)


class ClassBundleMenu(IMenu):
    def create(self):
        self.add(
            npyscreen.FixedText,
            value="Class Bundle Options",
            editable=False,
            color="STANDOUT",
        )

        self.bundle_options = self.add(
            npyscreen.TitleSelectOne,
            name="Bundle Options",
            values=[
                "Buy 5-Class Bundle",
                "Buy 10-Class Bundle",
                "Buy 20-Class Bundle",
                "Back to Plans",
                "Exit",
            ],
            scroll_exit=True,
            max_height=7,
        )

    def update_bundle_options(self):
        pass  # Placeholder for any dynamic updates if needed

    def on_ok(self):
        choice = self.bundle_options.value
        if not choice:
            npyscreen.notify_confirm(
                "Please select a bundle or press 'Back' to go back.",
                title="No Selection",
            )
            self.parentApp.switchForm(Form.CLASS_BUNDLE)
            return
        selected = choice[0]
        if selected in [0, 1, 2]:
            classes = [5, 10, 20]
            num_classes = classes[selected]
            npyscreen.notify_confirm(
                f"Thank you for purchasing the {num_classes}-Class Bundle!",
                title="Purchase Successful",
            )
            self.parentApp.switchForm(Form.MAIN)
        elif selected == 3:
            self.parentApp.switchForm(Form.SUBSCRIPTION)
        elif selected == 4:
            self.parentApp.setNextForm(None)

    def on_cancel(self):
        self.parentApp.switchForm(Form.SUBSCRIPTION)
