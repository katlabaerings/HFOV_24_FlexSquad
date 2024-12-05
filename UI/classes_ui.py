import os
import sys
from Logic.class_logic import ClassLogic

"""
# Dynamically add the parent directory to sys.path
script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(script_dir, ".."))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)
from Data.read_data import Data
from Logic.class_logic import get_all_classes
from datetime import datetime
"""

class UIclasses:
    def __init__(self):
        self.class_logic = ClassLogic()


    def get_all_classesUI(self):
        return self.class_logic.get_all_classesLOGIC()

    def add_member_to_classUI(self, member_id, class_id):
        return self.class_logic.add_member_to_classLOGIC(member_id, class_id)


    def display_all_classes():
    all_classes = get_all_classes()
    return_str = ""
    for a_class in all_classes:
        locality = False
        if a_class.locality == "L":
            locality = True
        
            return_str += f"               {a_class.class_name} 
                {a_class.date} At: {a_class.time} 
                Teached by: {a_class.trainer.firstname} {a_class.trainer.lastname}
                Virtual:{locality}
                "
    return return_str
        


'''
if __name__ == "__main__":
    display_all_classes()
    print("")
    print("")
    display_classes_today()
    print("Available classes:")
    display_available_classes()
'''
