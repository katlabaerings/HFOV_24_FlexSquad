import csv
import os

from Data.models.manager import Manager
from Data.models.member import Member
from Data.models.fitness_class import FitnessClass


class Data:
    CLASS_FILE_PATH = "../Data/class_data.csv"
    MANAGER_FILE_PATH = "../Data/manager_data.csv"
    MEMBER_FILE_PATH = "../Data/member_data.csv"
    SUBSCRIPTION_FILE_PATH = "../Data/subscription_data.csv"

    def class_by_id(self, id: int):
        with open(self.CLASS_FILE_PATH, mode="r") as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                if row["id"] == str(id):
                    row["trainer"] = self.manager_by_id(row["trainer_id"])
                    del row["trainer_id"]
                    return FitnessClass(**row)
                else:
                    continue
        return False

    def member_by_id(self, id: int):
        with open(self.MEMBER_FILE_PATH, mode="r") as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                if row["id"] == str(id):
                    return Member(**row)
                else:
                    continue
        return False

    def manager_by_id(self, id: int):
        with open(self.MANAGER_FILE_PATH, mode="r") as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                if row["id"] == str(id):  # Compare as string
                    return Manager(**row)

        return False
    
    def classes_by_emp_id(self, emp_id):
        with open(self.CLASS_FILE_PATH, mode="r") as file:
            csv_reader = csv.DictReader(file)
            classes = []
            for row in csv_reader:
                if row["trainer_id"] == str(emp_id):
                    classes.append(FitnessClass(row))
            return classes

