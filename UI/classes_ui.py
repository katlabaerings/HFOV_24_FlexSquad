from Data.read_data import Data
from Logic.class_logic import ClassLogic


class UIclasses:
    def __init__(self):
        self.class_logic = ClassLogic()


    def get_all_classesUI(self):
        return self.class_logic.get_all_classesLOGIC()
