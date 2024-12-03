import csv
import os

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

