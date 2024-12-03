import csv
import os
from Logic.find_class_by_id import Classes

def get_class_by_id(target_id):
    class_id = Classes(target_id).get_current_capacity_of_class()
    print(f"{class_id['class']}: {class_id['maxCapacity']}/{class_id['currentCapacity']}")

def main():
    class_id = input("Enter class id: ")
    get_class_by_id(int(class_id))

if __name__ == "__main__":
    main()

