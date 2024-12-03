from dataclasses import dataclass
import csv
from Data.read_data import manager_by_id

FILEPATH = "class_data.csv"


@dataclass
class FitnessClass:
    id: int = None
    name: str = None
    max_members: int = 0
    curr_num_members: int = 0
    members = []
    fitness_instructor: str = (None,)
    date: str = 0
    time: int = 0
    virtual: bool = False


def read_all_classes():
    classes = []
    with open(FILEPATH, mode="r") as file:
        csv_reader = csv.reader(file)
    for a_class in csv_reader:
        split = a_class.split(",")
        fitness_instructor = manager_by_id(split[5])
        data = {
            "id": split[0],
            "name": split[1],
            "max_members": split[2],
            "curr_num_members": split[3],
            "members": split[4],
            "fitness_instructor": fitness_instructor,
            "date": split[6],
            "time": split[7],
            "virtual": split[8],
        }

        fitness_class = FitnessClass(**data)
        classes.append(fitness_class)
