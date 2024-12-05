import csv
from tabulate import tabulate
import typing
from models.manager import Manager
from models.member import Member
from models.fitness_class import FitnessClass


class Data:
    CLASS_FILE_PATH = "./Data/class_data.csv"
    MANAGER_FILE_PATH = "./Data/manager_data.csv"
    MEMBER_FILE_PATH = "./Data/member_data.csv"
    SUBSCRIPTION_FILE_PATH = "./Data/subscription_data.csv"

    
    def class_by_id(self, id: int):
        """Takes in an id of a fitness class, and returns
        an instance of the Fitness class model class.

        Args:
            id (int): An integer representing the id of the fitness class.

        Returns:
            bool/FitnessClass: Returns an instance of FitnessClass or False if the fitness class 
            with the id does not exist in the database.
        """
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
        """Takes in an id of a member, and returns an instance of the Member model class.

        Args:
            id (int): An integer representing the id of the member.

        Returns:
            bool/Member: Returns an instance of a Member or False if the member with the id does not
            exist in the database.
        """
        with open(self.MEMBER_FILE_PATH, mode="r") as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                if row["id"] == str(id):
                    return Member(**row)
                else:
                    continue
        return False

    def manager_by_id(self, id: int):
        """Takes in an id of a manager, and returns an instance of the Manager model class.

        Args:
            id (int): An integer representing the id of the manager.

        Returns:
            bool/Manager: Returns an instance of a Manager or False if the manager with the id does not
            exist in the database.
        """
        with open(self.MANAGER_FILE_PATH, mode="r") as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                if row["id"] == str(id):  # Compare as string
                    return Manager(**row)

        return False

    def classes_by_emp_id(self, emp_id : int) -> list[FitnessClass]:
        """Takes in an id of the fitness_instructor, and returns a list of instances
        of FitnessClasses. All the FitnessClasses in the list are instructed by the 
        fitness instructor.

        Args:
            emp_id (int): An integer representing the id of the trainer.

        Returns:
            list[FitnessClass]: Returns a list of FitnessClass instances, or an empty list if 
            the fitness instructor is not teaching any fitness classes.
        """
        with open(self.CLASS_FILE_PATH, mode="r") as file:
            csv_reader = csv.DictReader(file)
            classes = []
            for row in csv_reader:
                if row["trainer_id"] == str(emp_id):
                    classes.append(FitnessClass(row))
            return classes

    def get_all_classes(self) -> list[FitnessClass]:
        """Opens and reads through the class database, makes instances of FitnessClasses and
        adds to a list. Returns the list.

        Returns:
            list[FitnessClass]: Returns a list of instances of the FitnessClass model class. If there
            are no FitnessClasses in the database it will return an empty list.
        """
        all_classes = []
        with open(self.CLASS_FILE_PATH, mode="r") as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                row["trainer"] = self.manager_by_id(row["trainer_id"])
                del row["trainer_id"]
                all_classes.append(FitnessClass(**row))
        return all_classes
         