import csv
import datetime
import os
from Data.read_data import Data

class Classes:
    def __init__(self, file_path, target_id, date):
        self.file_path = file_path
        self.target_id = target_id
        self.date = date
    
    def get_current_capacity_of_class(self):
        try:
            validated_date = datetime.datetime.strptime(self.date, "%d/%m/%Y")
        except ValueError:
            raise ValueError("The date format is invalid. It should be in the format DD/MM/YYYY.")
                
        data = Data(self.file_path, self.target_id, validated_date).class_by_id()
        return data



