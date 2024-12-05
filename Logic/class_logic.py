from datetime import datetime, timedelta
from Data.read_data import ReadData
from Data.write_data import WriteData

from Data.models.fitness_class import FitnessClass


class ClassLogic:
    def __init__(self):
        self.read = ReadData()
        self.write = WriteData()

    # This function is used to implement the user story:"As a gym member I want to be able to
    # book classes easily through platforms such as an app"
    def add_member_to_classLOGIC(self, member_id: int, class_id: int):
        # Calls the appropriate function to sign a member to a certain class.
        return self.write.add_member_to_classDATA(member_id, class_id)

    # This function is used to implement the user story: "As a fitness instructor I want to see
    # how many members are attending my class so that I can be better prepared for each class"
    def get_classes_by_trainer(self, trainer_id: int) -> list[FitnessClass]:
        """Returns a list of classes that the trainer with the id is
        teaching.

        Args:
            trainer_id (int): An integer representing the id of the trainer.

        Returns:
            list[FitnessClass]: Returns a list of FitnessClass instances
        """
        trainer = self.read.manager_by_id(trainer_id)

        # check to make sure if the manager exists, that it is of type 'trainer'
        if not trainer or trainer.type.lower() != "trainer":
            return []

        all_classes = self.read.get_all_classes()
        returning_classes = []
        for t_class in all_classes:
            if t_class.trainer_id == trainer.id:
                returning_classes.append(t_class)

        return returning_classes

    # This function is for the user story "As a gym member, I want to be able to attend virtual classes,
    # so I can keep working on my health and well-being, even though I can’t physically be there"
    # This function filters out all the classes that are virtual and returns a list of them.
    def get_virtual_classes(self):
        classes = self.read.get_all_classes()
        v_classes = []
        for f_class in classes:
            if f_class.locality == "V":
                v_classes.append(f_class)
        return v_classes

    def get_next_class(self, id):
        current_time = datetime.now()
        classes = self.data.get_all_classes()
        next_class = None
        for f_class in classes:
            members = f_class.members.split()  # Use dot notation to access attributes
            if id not in members:
                continue

            try:
                class_datetime = datetime.strptime(
                    f"{f_class.date} {f_class.time}", "%d.%m.%Y %H:%M"
                )
            except ValueError:
                # Skip classes with invalid dates or times
                continue

            # Compare to find the next upcoming class
            if class_datetime > current_time:
                if next_class is None or class_datetime < datetime.strptime(
                    f"{next_class.date} {next_class.time}", "%d.%m.%Y %H:%M"
                ):
                    next_class = f_class

        return next_class

    def is_class_within_next_hour(self, id):
        current_time = datetime.now()
        one_hour_later = current_time + timedelta(hours=1)

        classes = self.data.get_all_classes()
        for f_class in classes:
            # Check if the user is in the members list
            if id not in f_class.members.split():
                continue

            try:
                # Parse the class's date and time into a datetime object
                class_datetime = datetime.strptime(
                    f"{f_class.date} {f_class.time}", "%d.%m.%Y %H:%M"
                )
            except ValueError:
                # Skip classes with invalid dates or times
                continue

            # Check if the class is within the next hour
            if current_time <= class_datetime <= one_hour_later:
                return f_class  # Return the class if it is within the next hour

        return None
