from UI.subscription_menu import SubscriptionUI

import npyscreen


class MainMenuApp(npyscreen.NPSApp):
    def main(self):
        form = npyscreen.Form(
            name="City Gym Hub",
        )

        menu_title = form.add(
            npyscreen.FixedText,
            value="Welcome to City Gym Hub - where we are all about the gains!",
            editable=False,
            color="STANDOUT",
        )
        menu_title.centered = True

        menu_options = form.add(
            npyscreen.TitleSelectOne,
            name="Options",
            values=["View Subscription Plans", "Book A Class", "Exit"],
            scroll_exit=True,
        )

        form.edit()

        selected_option = menu_options.get_selected_objects()
        if selected_option:
            if "View Subscription Plans" in selected_option:
                self.show_subscription_plans()
            elif "Book a Class" in selected_option:
                self.book_class()
            elif "Exit" in selected_option:
                self.exit_app()

    def show_subscription_plans(self):
        subscription_ui = SubscriptionUI()
        subscription_ui.show_plan_details()

    def book_class(self):
        npyscreen.notify_confirm("Feature coming soon!", title="Book a Class")

    def exit_app(self):
        npyscreen.notify_confirm("Goodbye!", title="Exit")
