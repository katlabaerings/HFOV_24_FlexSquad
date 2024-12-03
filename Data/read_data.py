import csv
import os


def class_by_id(file_path, target_id):
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if row['id'] == str(target_id):  # Compare as string
                return row
        

if __name__ == "__main__":
    class_by_id("../Data/class_data.csv", 1)