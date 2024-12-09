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
    def add_member_to_class(self, member_id: int, class_id: int):
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
        # if not trainer or trainer.type.lower() != "trainer":
        #     return []

        all_classes = self.read.get_all_classes()
        returning_classes = []
        for t_class in all_classes:
            if t_class.trainer_id.id == trainer_id:
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
        classes = self.read.get_all_classes()
        next_class = None

        for f_class in classes:
            # Ensure members are split properly
            members = f_class.members.split() if f_class.members else []
            # Check if id is in members
            if str(id) not in members:
                continue
            try:
                # Parse datetime from date and time
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

        classes = self.read.get_all_classes()
        for f_class in classes:
            # Ensure members are properly split and checked
            members = f_class.members.split() if f_class.members else []
            if str(id) not in members:  # Compare as strings
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
    
    # These following functions (get_member_by_id, calculate_loyalty_points and get_loyalty_rewards)
    # are for the user story: "As a long-term gym member, I want to be rewarded for being 
    # a loyal customer to help me stay motivated on my fitness journey"
    def get_member_by_id(self, user_id: int):
        try:
            member = self.read.member_by_id(user_id)
            return member
        except Exception as e:
            print(f"Error retrieving member with ID {user_id}: {e}")
            return None
    
    def calculate_loyalty_points(self, joined_date: str) -> int:
        """Calculate loyalty points based on the member's join date."""
        try:
            join_date = datetime.strptime(joined_date, "%Y-%m-%d")
            years_as_member = (datetime.now() - join_date).days // 365
            return years_as_member * 10  # 10 points per year
        except ValueError:
            return 0
    
    def get_loyalty_rewards(self, points: int) -> str:
        """Determine rewards based on loyalty points."""
        if 10 <= points <= 20:
            return "Enjoy one free juice at the Boozt Bar"
        elif 30 <= points <= 40:
            return "Enjoy one free juice at the Boozt Bar and a personalized food plan"
        elif points >= 50:
            return "Enjoy one free juice at the Boozt Bar, a personalized food plan, and a one-on-one personal trainer session"
        else:
            return "No rewards yet, but starting your second year with us, you'll earn rewards every year!"
 
