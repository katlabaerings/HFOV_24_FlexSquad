import npyscreen
from Logic.class_logic import get_virtual_classes

class VirtualClassForm(npyscreen.ActionForm):
    def create(self):
        self.add(npyscreen.FixedText, value="Virtual Class", editable=False, color="STANDOUT")



    def on_cancel(self):  # This method is called when "Cancel" is pressed
        self.parentApp.switchForm('MAIN')