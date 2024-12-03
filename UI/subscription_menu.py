from Logic.subscription_logic import get_subscription_plans, get_plan_details
import npyscreen


class SubscriptionUI:
    def display_subscription_options(self):
        return get_subscription_plans()

    def show_plan_details(self):
        plans = self.display_subscription_options()
        plan_names = [plan["PlanName"] for plan in plans]

        form = npyscreen.Form(name="Subscription Plans")
        selected_plan = form.add(
            npyscreen.TitleSelectOne,
            name="Available Plans",
            values=plan_names,
            scroll_exit=True,
        )
        form.edit()

        if selected_plan.value is not None:
            selected_plan_name = plan_names[selected_plan.value[0]]
            self.show_selected_plan_details(selected_plan_name)

    def show_selected_plan_details(self, selected_plan_name):
        details = get_plan_details(selected_plan_name)
        npyscreen.notify_confirm(details, title=f"Plan Details: {selected_plan_name}")

        if selected_plan_name == "Class Bundle":
            self.display_class_bundle_options()
        else:
            self.display_post_plan_options(selected_plan_name)

    def display_post_plan_options(self, selected_plan):
        """Post-plan selection options."""
        form = npyscreen.ActionPopup(name=f"{selected_plan} Options")
        actions = form.add(
            npyscreen.TitleSelectOne,
            name="Options",
            values=["Buy Plan", "Back to Plans", "Exit"],
            scroll_exit=True,
        )
        form.edit()

        if actions.value is not None:
            if actions.value[0] == 0:
                npyscreen.notify_confirm(
                    f"Thank you for choosing to buy the {selected_plan}!",
                    title="Purchase Successful",
                )
            elif actions.value[0] == 1:
                self.show_plan_details()
            elif actions.value[0] == 2:
                npyscreen.notify_confirm("Goodbye!", title="Exit")

    def display_class_bundle_options(self):
        form = npyscreen.ActionPopup(name="Class Bundle Options")
        actions = form.add(
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
        )
        form.edit()

        if actions.value is not None:
            choice = actions.value[0]
            if choice in [0, 1, 2]:
                npyscreen.notify_confirm(
                    f"Thank you for purchasing the {5 * (choice + 1)}-Class Bundle!",
                    title="Purchase Successful",
                )
            elif choice == 3:
                self.show_plan_details()
            elif choice == 4:
                npyscreen.notify_confirm("Goodbye!", title="Exit")
