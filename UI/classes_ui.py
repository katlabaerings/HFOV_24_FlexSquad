import os
import sys
from Logic.class_logic import ClassLogic, get_all_classes

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


def display_all_classes():
    all_classes = get_all_classes()
    return_str = []
    for a_class in all_classes:
        locality = False
        if a_class.locality == "L":
            locality = True
            
        return_str.append(f"{a_class.class_name} {a_class.date} At: {a_class.time} Teached by: {a_class.trainer.firstname} {a_class.trainer.lastname} Virtual:{locality}")
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
