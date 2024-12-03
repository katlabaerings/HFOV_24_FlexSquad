import csv
import os
from Data.read_data import Data

class Classes:
    def __init__(self, target_id):
        self.target_id = target_id
    
    def get_current_capacity_of_class(self):
        data = Data().class_by_id(self.target_id)
       # classId = class_by_id(self.file_path, self.target_id)
        return data
    
    def get_classes_by_emp_id(self):
        data = Data().classes_by_emp_id(self.target_id)
        return data



