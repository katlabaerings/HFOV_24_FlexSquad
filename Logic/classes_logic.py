from dataclasses import dataclass
import csv
from Data.read_data import manager_by_id, Data

def read_all_classes():
        data = Data()
        classes = []
        while member := data.class_by_id():
                pass
