import npyscreen

from UI.Menus.book_class import BookClassMenu
from UI.Menus.class_menu import AllClassesMenu, ClassesTodayMenu, PickClassMenu
from UI.Menus.subscription_menu import (
    SubscriptionMenu,
    PostPlanOptionsMenu,
    ClassBundleMenu,
)
from UI.Menus.trainer_menu import TrainerMenuForm, ClassMenuForm
from UI.Menus.main_menu import MainMenu
from UI.Menus.login_menu import LoginMenu
from UI.Menus.virtual_menu import VirtualMenu
from UI.form_enums import Form


class GymApp(npyscreen.NPSAppManaged):
    user_id = None

    def onStart(self):
        # Register Forms
        self.addForm(Form.LOGIN, LoginMenu, name="City Gym Hub Login")
        self.addForm(Form.MAIN, MainMenu, name="City Gym Hub")
        self.addForm(Form.SUBSCRIPTION, SubscriptionMenu, name="Subscription Plans")
        self.addForm(Form.PICK_CLASS, PickClassMenu, name="Pick Class Option")
        self.addForm(Form.ALL_CLASS, AllClassesMenu, name="All Classes")
        self.addForm(Form.CLASS_TODAY, ClassesTodayMenu, name="Classes Today")
        self.addForm(Form.BOOK_CLASS, BookClassMenu, name="Book Class")
        self.addForm(Form.CLASS_MENU, VirtualMenu, name="Virtual Menu")
        self.addForm(Form.POST_PLAN, PostPlanOptionsMenu, name="Post Plan Options")
        self.addForm(Form.CLASS_BUNDLE, ClassBundleMenu, name="Class Bundle Options")
        self.addForm(Form.TRAINER, TrainerMenuForm, name="View Classes by Trainer")
        self.addForm(Form.CLASS_MENU, ClassMenuForm, name="Class Menu")

        self.setNextForm(Form.LOGIN)

    def onCleanExit(self):
        npyscreen.notify_confirm("Exiting application. Goodbye!", title="Exit")


if __name__ == "__main__":
    app = GymApp().run()
