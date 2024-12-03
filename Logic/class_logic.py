import csv
import os

def load_classes():
    all_classes = []
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, '../Data/class_data.csv')
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            all_classes.append(row)
    return all_classes

def get_virtual_classes(class_list):
    ret_lis = []
    for i in class_list:
        if i['locality'] == 'V':
            ret_lis.append(i)
    return ret_lis


