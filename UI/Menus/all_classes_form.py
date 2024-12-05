import npyscreen

from UI.classes_ui import display_all_classes


class AllClassesForm(npyscreen.ActionForm):
    def create(self):
        classes_string = display_all_classes()
        for class_str in classes_string:
            self.add(npyscreen.TitleFixedText, name=class_str)

    def on_ok(self):
        self.parentApp('MAIN')


    def on_cancel(self):
        self.parentApp.switchForm('MAIN')