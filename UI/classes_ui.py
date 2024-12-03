from Data.read_data import Data
from Logic.class_logic import get_all_classes


def display_all_classes():
    all_classes = get_all_classes()
    for a_class in all_classes:
        print(
            f"""{a_class.class_name} 
                {a_class.date} At: {a_class.time} 
                Teached by: {a_class.trainer.firstname} {a_class.trainer.lastname}
"""
        )


if __name__ == "__main__":
    display_all_classes()

