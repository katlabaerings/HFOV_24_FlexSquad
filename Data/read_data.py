import csv
import os


class Data:
    CLASS_FILE_PATH = "Data/class_data.csv"
    MANAGER_FILE_PATH = "Data/manager_data.csv"
    MEMBER_FILE_PATH = "Data/member_data.csv"
    SUBSCRIPTION_FILE_PATH = "Data/subscription_data.csv"

    def class_by_id(self, id: int):
        with open(self.CLASS_FILE_PATH, mode="r") as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                if row["id"] == str(id):
                    return row
                else:
                    continue

    def member_by_id(self, id: int):
        with open(self.MEMBER_FILE_PATH, mode="r") as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                if row["id"] == str(id):
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


