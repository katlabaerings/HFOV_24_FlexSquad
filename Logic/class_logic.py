import csv
import os
from Data.read_data import Data
from Data.write_data import WriteData


class ClassLogic:
    def __init__(self):
        self.data = Data()
        self.write = WriteData()



    def get_virtual_classes(self):
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


    def add_member_to_classLOGIC(self, member_id, class_id):
        return self.write.add_member_to_classDATA(member_id, class_id)

    def sign_up_for_a_class(self,class_id : int, member_id : int):
        the_class = self.data.class_by_id(class_id)
        the_class.members.append(member_id)

<<<<<<< Updated upstream
=======
    

    
>>>>>>> Stashed changes
    def get_all_classes(self):
        classes = []
        i = 1
        while fitness_class := self.data.class_by_id(i):
            classes.append(fitness_class)
            i += 1
        return classes

    def get_classes_by_trainer(self,trainer_id: int):
        all_classes = self.get_all_classes()
        returning_classes = []
        for clas in all_classes:
            if clas.trainer.id == trainer_id:
                returning_classes.append(clas)
        return returning_classes


    def get_virtual_classes(self):
        classes = self.get_all_classes()
        v_classes = []
        for f_class in classes:
            if f_class.locality == 'V':
                v_classes.append(f_class)
        return v_classes




