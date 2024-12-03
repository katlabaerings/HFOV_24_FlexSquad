import csv
import os
import npyscreen
from Logic.find_class_by_id import Classes

def get_class_by_id(employee_id):
    employee_classes = Classes(employee_id).get_current_capacity_of_class()
    return employee_classes
    # form = npyscreen.Form(name="Classes")
    # menu_title = form.add(
    #         npyscreen.FixedText,
    #         value=employee_classes.class_name,
    #         editable=False,
    #         color="STANDOUT",
    #     )
    # menu_title.centered = True

def main():
    employee_id = input("What is your id: ")
    get_class_by_id(int(employee_id))

if __name__ == "__main__":
    main()

