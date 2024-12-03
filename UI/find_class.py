import csv
import os
from Logic.find_class_by_id import Classes

def get_class_by_id(file_path, target_id):
    classId = Classes(file_path, target_id).get_current_capacity_of_class()
    print(f"{classId['class']}: {classId['maxCapacity']}/{classId['currentCapacity']}")

def main():
    class_id = input("Enter class id: ")
    get_class_by_id("../Data/class_data.csv",int(class_id))

if __name__ == "__main__":
    main()

