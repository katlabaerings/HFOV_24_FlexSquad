import npyscreen

from UI.Menus.all_classes_form import AllClassesForm
from UI.Menus.main_menu import MainMenu
from UI.Menus.subscription_menu import SubscriptionForm, PostPlanOptionsForm, ClassBundleForm
from UI.Menus.trainer_menu import TrainerMenuForm, ClassMenuForm
from UI.Menus.virtual_class_ui import VirtualClassForm


class GymApp(npyscreen.NPSAppManaged):
    def onStart(self):
        # Register Forms
        self.addForm('MAIN', MainMenu, name="City Gym Hub")
        self.addForm('SUBSCRIPTION', SubscriptionForm, name="Subscription Plans")
        self.addForm('ALL_CLASS', AllClassesForm, name="All Classes" )
        self.addForm('POST_PLAN', PostPlanOptionsForm, name="Post Plan Options")
        self.addForm('CLASS_BUNDLE', ClassBundleForm, name="Class Bundle Options")
        self.addForm('TRAINER', TrainerMenuForm, name="Trainer Menu")
        self.addForm('CLASS_MENU', ClassMenuForm, name="Class Menu")
        self.addForm('VIRTUAL_CLASS', VirtualClassForm, name='Virtual Class Menu')

    def onCleanExit(self):
        npyscreen.notify_confirm("Exiting application. Goodbye!", title="Exit")


if __name__ == "__main__":
    app = GymApp().run()
