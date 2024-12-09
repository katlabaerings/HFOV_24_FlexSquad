#Wadda frick is this

import os
import sys

# Dynamically add the parent directory to sys.path
script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(script_dir, '..'))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)


from Logic.class_logic import get_virtual_classes
import webbrowser
import time


class VirtualClasses:
    def __init__(self) -> None:
        self.virtual_classes = get_virtual_classes()

    def get_class_by_name(self, aName):
        for aClass in self.virtual_classes:
            if aClass.class_name == aName:
                return aClass

    def run_class(self, aClass):
        print('Welcome...')
        time.sleep(1)
        print(f'Please wait for the class to start...')
        time.sleep(2)
        webbrowser.open(aClass.link)


def main():
    a_virtual = VirtualClasses()
    prump = a_virtual.get_class_by_name('Moonwalking competition')
    a_virtual.run_class(prump)


if __name__ == '__main__':
    main()