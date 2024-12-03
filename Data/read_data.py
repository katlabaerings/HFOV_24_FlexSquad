import csv
import os
import datetime

class Data:
    def __init__(self, file_path, target_id, date):
        self.file_path = file_path
        self.target_id = target_id
        self.date = date

    def class_by_id(self):
        with open(self.file_path, mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                if row['id'] == str(self.target_id) and row['date'] == self.date.strftime("%d/%m/%Y"): 
                    return row
                else:
                    continue
