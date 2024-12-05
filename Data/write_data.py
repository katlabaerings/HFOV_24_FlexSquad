import csv

from Data.read_data import Data


#This class is for implementing the user story:"As a gym member
#I want to be able to book classes easily through platforms such as an app."
class WriteData:
    def __init__(self):
        self.data = Data()
        self.CLASS_FILE_PATH = "../Data/class_data.csv"
        self.MANAGER_FILE_PATH = "../Data/manager_data.csv"
        self.MEMBER_FILE_PATH = "../Data/member_data.csv"
        self.SUBSCRIPTION_FILE_PATH = "../Data/subscription_data.csv"



    def add_member_to_classDATA(self, member_id :int, class_id: int):
        try:
            # Validate class and member IDs
            self.data.class_by_id(class_id)
            self.data.member_by_id(member_id)
        except Exception: # TODO: Specify exception
            return "Class or member does not exist"

        all_classes = self.data.get_all_classes()

        # Modify the relevant class
        for a_class in all_classes:
            if a_class.id == class_id:
                # Check if class is already at max capacity
                if a_class.current_capacity >= a_class.max_capacity:
                    return "Cannot add member: class is at maximum capacity."
                # Update current capacity
                a_class.current_capacity += 1
                # Update members list
                a_class.members.append(member_id)
                self.updated_classes(a_class)
        else:
            # If class_id not found in CSV
            return "Class not found in the CSV file."

    def to_CSV(self, a_class : FitnessClass) -> dict:
        """This function takes in an instance of a FitnessClass,
        unpacks its attributes and adds it to a dictionary.

        Args:
            a_class (FitnessClass): An instance of a FitnessClass.

        Returns:
            dict: Returns a dict with all the fields as keys and the attributes as the value.
        """
        return {
            "id": a_class.id,
            "class_name": a_class.name,
            "max_capacity": a_class.max_capacity,
            "current_capacity": a_class.current_capacity,
            "members": a_class.members,
            "trainer_id": a_class.trainer_id,
            "time": a_class.time,
            "date": a_class.date,
            "locality": a_class.locality,
            "link":a_class.link
        }


    def update_classes(self,updated_class : FitnessClass) -> None:
        """Writes all the classes down to the database, with the updated data.

        Args:
            updated_class (FitnessClass): Takes in an updated instance of a fitness class.

        """
        all_classes = self.get_all_classes()
        for i, _class in enumerate(all_classes):
            if _class.id == updated_class.id:
                all_classes[i] = updated_class
                break

        with open(self.CLASS_FILE_PATH, mode="w", newline='') as file:
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
                "link"
            ]
            csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
            csv_writer.writeheader()
            for a_class in all_classes:
                writer.writerow(self.to_CSV(a_class))

        return f"Member {member_id} added to class {class_id}."


