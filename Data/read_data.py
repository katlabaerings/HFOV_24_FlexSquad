import csv
import os


class Data:
    def __init__(self, file_path, target_id):
        self.file_path = file_path
        self.target_id = target_id
        self.MANAGER_FILE_PATH = "manager_data.csv"

    def class_by_id(self):
        with open(self.file_path, mode="r") as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                if row["id"] == str(self.target_id):
                    return row
                else:
                    continue

    def manager_by_id(self, id: int):
        with open(self.MANAGER_FILE_PATH, mode="r") as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                if row["id"] == str(id):  # Compare as string
                    return row


MANAGER_FILE_PATH = "manager_data.csv"


def manager_by_id(id: int, file_path=MANAGER_FILE_PATH):
    with open(file_path, mode="r") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if row["id"] == str(id):  # Compare as string
                return row


# if __name__ == "__main__":
#     class_by_id("../Data/class_data.csv", 1)
