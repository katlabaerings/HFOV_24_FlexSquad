import csv
import os
from Logic.find_classes import Classes

def get_class_by_id(file_path, target_id,date):
    classId = Classes(file_path, target_id, date).get_current_capacity_of_class()
    if classId == None:
        print(f"no class this day with {target_id} id or {target_id} invalid!")
    else:
        print(f" {classId['date']} {classId['class']}: {classId['currentCapacity']}/{classId['maxCapacity']}")

def main():
    class_id = input("Enter class id: ")
    date = input("Enter date: ")
    file = "../Data/class_data.csv"
    get_class_by_id(file,int(class_id),date)

if __name__ == "__main__":
    main()

