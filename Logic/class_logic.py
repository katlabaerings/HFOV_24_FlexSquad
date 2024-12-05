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
        returning_classes = [
            t_class for t_class in all_classes if int(t_class.trainer_id) == trainer.id
        ]

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
