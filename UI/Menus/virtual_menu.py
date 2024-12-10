import npyscreen
from UI.interfaces.i_menu import IMenu
from UI.form_enums import Form
from Logic.class_logic import ClassLogic

'''This is the interface that lets users select what virtual class to attend'''

class VirtualMenu(IMenu):
    def create(self):
        self.classes_status = self.add(
                npyscreen.TitleText, name="Select Virtual Class", color="STANDOUT"
            )
        virtual_classes = self.fetch_virtual_classes_by_id(self.parentApp.user_id)
        for a_class in virtual_classes:
            self.add(npyscreen.TitleFixedText, name=a_class.class_name)

        
    def fetch_virtual_classes_by_id(self, id):
        ret_lis = []
        class_logic = ClassLogic()
        all_classes = class_logic.get_virtual_classes()
        for a_class in all_classes:
            if id in a_class.members.split():
                ret_lis.append(a_class)
        return ret_lis
    
    def on_ok(self):
        pass


    def on_cancel(self):
        return super().on_cancel()
    