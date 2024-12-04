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