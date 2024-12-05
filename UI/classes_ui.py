import os
import sys
from datetime import datetime

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
class_logic = ClassLogic()


def display_all_classes():
    all_classes = class_logic.get_all_classes()
    return_str = []
    for a_class in all_classes:
        locality = False
        if a_class.locality == "L":
            locality = True

        return_str.append(
            f"{a_class.class_name} {a_class.date} At: {a_class.time} Teached by: {a_class.trainer.firstname} {a_class.trainer.lastname} Virtual:{locality}")
    return return_str



        


def display_classes_today():
    today = datetime.today()
    year = today.year
    month = today.month
    day = today.day
    formatted_date = f"{day}.{month}.{year}"
    all_classes = get_all_classes()
    for a_class in all_classes:
        locality = False
        if a_class.locality == "L":
            locality = True
        if a_class.date == formatted_date:
            print(
                f"""                 {a_class.class_name}
                 Teached by:{a_class.trainer.firstname}{a_class.trainer.lastname}
                 Virtual:{locality}
                 Bookings:{a_class.current_capacity}/{a_class.max_capacity}"""
            )


def display_available_classes():
    all_classes = get_all_classes()
    for a_class in all_classes:
        locality = False
        if a_class.locality == "L":
            locality = True
        if int(a_class.max_capacity) > int(a_class.current_capacity):
            print(
                f"""                {a_class.class_name} 
                {a_class.date} At: {a_class.time} 
                Teached by: {a_class.trainer.firstname} {a_class.trainer.lastname}
                Virtual:{locality}
                Bookings:{a_class.current_capacity}/{a_class.max_capacity}
"""
            )
