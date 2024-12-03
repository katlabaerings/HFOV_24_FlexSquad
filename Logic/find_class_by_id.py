import csv
import os
from Data.read_data import class_by_id

def main():
    print("halló")
    find_class("../Data/class_data.csv",1)


def find_class(file_path, target_id):
    classId = class_by_id(file_path, target_id)
    return classId

if __name__ == "__main__":
    main()

