from datetime import datetime
from Data.read_data import Data


data = Data()


def display_all_classes():
    all_classes = data.get_all_classes()
    return_str = []
    for a_class in all_classes:
        locality = False
        if a_class.locality == "L":
            locality = True

        return_str.append(
            f"{a_class.class_name} {a_class.date} At: {a_class.time} Taught by: {a_class.trainer.firstname} {a_class.trainer.lastname} Virtual:{locality}"
        )
    return return_str


def display_classes_today():
    today = datetime.today()
    year = today.year
    month = today.month
    day = today.day
    formatted_date = f"{day}.{month}.{year}"
    all_classes = data.get_all_classes()
    all_classes = data.get_all_classes()
    return_str = []
    for a_class in all_classes:
        locality = False
        if a_class.locality == "L":
            locality = True
        if a_class.date == formatted_date:
            return_str.append(
                f"{a_class.class_name} Taught by:{a_class.trainer.firstname}{a_class.trainer.lastname} Virtual:{locality} Bookings:{a_class.current_capacity}/{a_class.max_capacity}"
            )
    return return_str


def display_available_classes():
    all_classes = data.get_all_classes()
    for a_class in all_classes:
        locality = False
        if a_class.locality == "L":
            locality = True
        if int(a_class.max_capacity) > int(a_class.current_capacity):
            print(
                f"""                {a_class.class_name} 
                {a_class.date} At: {a_class.time} 
                Taught by: {a_class.trainer.firstname} {a_class.trainer.lastname}
                Virtual:{locality}
                Bookings:{a_class.current_capacity}/{a_class.max_capacity}
"""
            )


def sign_up_for_a_class():
    display_available_classes()
    # Get an input from the user for what class we want to sign up to.
    data.sign_up_for_a_class(member_id, class_id)
