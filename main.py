import npyscreen

from UI.Menus.class_menu import AllClassesMenu, ClassesTodayMenu, PickClassMenu
from UI.Menus.subscription_menu import (
    SubscriptionForm,
    PostPlanOptionsForm,
    ClassBundleForm,
)
from UI.Menus.trainer_menu import TrainerMenuForm, ClassMenuForm
from UI.Menus.main_menu import MainMenu
from UI.Menus.login_menu import LoginMenu
from UI.form_enums import Form


class GymApp(npyscreen.NPSAppManaged):
    user_id = None

    def onStart(self):
        # Register Forms
        self.addForm(Form.LOGIN, LoginMenu, name="City Gym Hub Login")
        self.addForm(Form.MAIN, MainMenu, name="City Gym Hub")
        self.addForm(Form.SUBSCRIPTION, SubscriptionForm, name="Subscription Plans")
        self.addForm(Form.PICK_CLASS, PickClassMenu, name="Pick Class Option")
        self.addForm(Form.ALL_CLASS, AllClassesMenu, name="All Classes")
        self.addForm(Form.CLASS_TODAY, ClassesTodayMenu, name="Classes Today")
        self.addForm(Form.POST_PLAN, PostPlanOptionsForm, name="Post Plan Options")
        self.addForm(Form.CLASS_BUNDLE, ClassBundleForm, name="Class Bundle Options")
        self.addForm(Form.TRAINER, TrainerMenuForm, name="Trainer Menu")
        self.addForm(Form.CLASS_MENU, ClassMenuForm, name="Class Menu")

        self.setNextForm(Form.LOGIN)

    def onCleanExit(self):
        npyscreen.notify_confirm("Exiting application. Goodbye!", title="Exit")


if __name__ == "__main__":
    app = GymApp().run()
