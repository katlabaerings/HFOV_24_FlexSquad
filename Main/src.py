from Data.read_data import Data
from UI.classes_ui import UIclasses
if __name__ == "__main__":
    # Write_data = WriteData()
    # Write_data.add_member_to_class (member_id=5, class_id=1)
    # test = Data()
    # print(test.get_all_classesDATA())
    test2 = UIclasses()
    print(test2.get_all_classesUI())
    test2.add_member_to_classUI(member_id=6, class_id=1)
    print(test2.get_all_classesUI())

