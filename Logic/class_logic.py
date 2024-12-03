import csv
import os

from Data.read_data import Data


# def get_virtual_classes():
#     all_classes = []
#     script_dir = os.path.dirname(__file__)
#     file_path = os.path.join(script_dir, '../Data/class_data.csv')
#     with open(file_path, newline='') as csvfile:
#         reader = csv.DictReader(csvfile)
#         for row in reader:
#             all_classes.append(row)
#     ret_lis = []
#     for i in all_classes:
#         if i['locality'] == 'V':
#             ret_lis.append(i)
#     return ret_lis

def read_all_classes():
        data = Data()
        classes = []
        i = 1
        while fitness_class := data.class_by_id(i):
            classes.append(fitness_class)
            i += 1
        return classes

def get_virtual_classes():
    classes = read_all_classes()
    v_classes = []
    for f_class in classes:
        if f_class.locality == 'V':
            v_classes.append(f_class)
    return v_classes
