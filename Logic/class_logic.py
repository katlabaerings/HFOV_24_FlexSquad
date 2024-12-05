import csv
import os
from Data.read_data import Data
from Data.write_data import WriteData


class ClassLogic:
    def __init__(self):
        self.data = Data()
        self.write = WriteData()


    @staticmethod
    def get_virtual_classes():
        all_classes = []
        script_dir = os.path.dirname(__file__)
        file_path = os.path.join(script_dir, '../Data/class_data.csv')
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                all_classes.append(row)
        ret_lis = []
        for i in all_classes:
            if i['locality'] == 'V':
                ret_lis.append(i)
        return ret_lis


    def get_all_classesLOGIC(self):
        # try:
        return self.data.get_all_classesDATA()
        # except Exception:
        #     return "no classes found..."

    def add_member_to_classLOGIC(self, member_id, class_id):
        return self.write.add_member_to_classDATA(member_id, class_id)




def get_all_classes():
    data = Data()
    classes = []
    i = 1
    while fitness_class := data.class_by_id(i):
        classes.append(fitness_class)
        i += 1
    return classes


def get_classes_by_trainer(trainer_id: int):
    all_classes = get_all_classes()
    returning_classes = []
    for clas in all_classes:
        if clas.trainer.id == trainer_id:
            returning_classes.append(clas)
    return returning_classes


def get_virtual_classes():
    classes = get_all_classes()
    v_classes = []
    for f_class in classes:
        if f_class.locality == 'V':
            v_classes.append(f_class)
    return v_classes

