import csv

from Data.read_data import ReadData
from Data.models.fitness_class import FitnessClass
import npyscreen


class WriteData:
    def __init__(self):
        self.data = ReadData()
        self.CLASS_FILE_PATH = "./Data/db/class_data.csv"
        self.MANAGER_FILE_PATH = "./Data/db/manager_data.csv"
        self.MEMBER_FILE_PATH = "./Data/db/member_data.csv"
        self.SUBSCRIPTION_FILE_PATH = "./Data/db/subscription_data.csv"

    def add_member_to_classDATA(self, member_id: int, class_id: int):

        all_classes = self.data.get_all_classes()
        # Modify the relevant class
        for a_class in all_classes:
            if int(a_class.id) == class_id:
                # Check if class is already at max capacity
                if a_class.current_capacity >= a_class.max_capacity:
                    return "Cannot add member: class is at maximum capacity."

                # Update current capacity
                a_class.current_capacity = int(a_class.current_capacity) + 1

                # Update members list correctly
                if a_class.members == "?":
                    a_class.members = str(member_id)
                else:
                    a_class.members = f"{a_class.members} {member_id}"  # Changed from member_id.trainer_id.id

                # Update the class in all_classes and write to file
                self.update_classes(a_class, all_classes)
                return "Successfully added member to class"

        return "Class not found in the CSV file."

    def to_CSV(self, a_class: FitnessClass) -> dict:
        return {
            "id": a_class.id,
            "class_name": a_class.class_name,
            "max_capacity": a_class.max_capacity,
            "current_capacity": a_class.current_capacity,
            "members": a_class.members,
            "trainer_id": a_class.trainer_id.id,  # Extract only the ID
            "time": a_class.time,
            "date": a_class.date,
            "locality": a_class.locality,
            "link": a_class.link,
        }

    def update_classes(
        self, updated_class: FitnessClass, all_classes: list[FitnessClass]
    ) -> None:
        """Writes all the classes down to the database, with the updated data."""
        # Update the class in the list directly
        for i, _class in enumerate(all_classes):
            if _class.id == updated_class.id:
                all_classes[i] = updated_class
                break  # Exit loop after updating

        with open(self.CLASS_FILE_PATH, mode="w", newline="") as file:
            fieldnames = [
                "id",
                "class_name",
                "max_capacity",
                "current_capacity",
                "members",
                "trainer_id",
                "time",
                "date",
                "locality",
                "link",
            ]
            csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
            csv_writer.writeheader()
            for a_class in all_classes:
                csv_writer.writerow(self.to_CSV(a_class))
