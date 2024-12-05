import csv
from tabulate import tabulate

from Data.models.manager import Manager
from Data.models.member import Member
from Data.models.fitness_class import FitnessClass


class Data:
    CLASS_FILE_PATH = "./Data/class_data.csv"
    MANAGER_FILE_PATH = "./Data/manager_data.csv"
    MEMBER_FILE_PATH = "./Data/member_data.csv"
    SUBSCRIPTION_FILE_PATH = "./Data/subscription_data.csv"

    def __init__(self):
        pass

    def class_by_id(self, id: int):
        with open(self.CLASS_FILE_PATH, mode="r") as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                if row["id"] == str(id):
                    trainer = self.manager_by_id(row["trainer_id"]) 
                    row["trainer_id"] = trainer.id if trainer else None 
                    fitness_class = FitnessClass(**row)
                    return fitness_class
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

    def get_all_classesDATA(self):
        all_classes = []
        with open(self.CLASS_FILE_PATH, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                all_classes.append(row)

        # Generate ASCII table
        headers = ["ID", "Class Name", "Max Capacity", "Current Capacity",
                   "Members", "Trainer", "Time", "Date", "Locality", "Link"]
        table_data = [
            [
                row['id'],
                row['class_name'],
                row['max_capacity'],
                row['current_capacity'],
                row['members'],
                self.manager_by_id(row['trainer_id']).firstname if hasattr(self.manager_by_id(row['trainer_id']),
                                                                           'firstname') else "Trainer not found",
                row['time'],
                row['date'],
                "Virtual" if row['locality'] == "V" else "Local" if row['locality'] == "L" else row['locality'],
                row['link']
            ]

            for row in all_classes
        ]
        table = tabulate(table_data, headers=headers, tablefmt="fancy_grid")
        return table
