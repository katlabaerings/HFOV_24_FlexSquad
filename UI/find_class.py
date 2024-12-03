import csv
import os
from Logic.find_class_by_id import find_class

def get_class_by_id(file_path, target_id):
    classId = find_class(file_path, target_id)
    # print(classId['class']":" classId['maxCapacity']"/")
    print(f"{classId['class']}: {classId['maxCapacity']}/{classId['currentCapacity']}")


if __name__ == "__main__":
    get_class_by_id("../Data/class_data.csv",1)

