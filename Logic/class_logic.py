import csv
import os

from Data.read_data import Data

def get_all_classes():
        data = Data()
        classes = []
        i = 1
        while fitness_class := data.class_by_id(i):
            classes.append(fitness_class)
            i += 1
        return classes

def get_virtual_classes():
    classes = get_all_classes()
    v_classes = []
    for f_class in classes:
        if f_class.locality == 'V':
            v_classes.append(f_class)
    return v_classes
