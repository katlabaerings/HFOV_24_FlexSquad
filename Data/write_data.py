import csv

from Data.read_data import Data



class WriteData:
    def __init__(self):
        self.data = Data()
        self.CLASS_FILE_PATH = "../Data/class_data.csv"
        self.MANAGER_FILE_PATH = "../Data/manager_data.csv"
        self.MEMBER_FILE_PATH = "../Data/member_data.csv"
        self.SUBSCRIPTION_FILE_PATH = "../Data/subscription_data.csv"



    def add_member_to_class(self, member_id, class_id):
        try:
            # Validate class and member IDs
            self.data.class_by_id(class_id)
            self.data.member_by_id(member_id)
        except Exception:
            return "Class or member does not exist"

        # Read all rows from the CSV file
        classes = []
        with open(self.CLASS_FILE_PATH, mode="r", newline='', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            fieldnames = csv_reader.fieldnames
            classes = list(csv_reader)

        # Modify the relevant row
        for row in classes:
            if row["id"] == str(class_id):
                max_capacity = int(row["max_capacity"])
                current_capacity = int(row["current_capacity"])

                # Check if class is already at max capacity
                if current_capacity >= max_capacity:
                    return "Cannot add member: class is at maximum capacity."

                # Update current capacity
                current_capacity += 1
                row["current_capacity"] = str(current_capacity)

                # Update members list
                member_list = row["members"]
                delimiter = "|"
                if member_list in ('?', '', None):
                    row["members"] = f"{member_id}"
                else:
                    row["members"] += f"{delimiter}{member_id}"
                break  # Exit after updating the class
        else:
            # If class_id not found in CSV
            return "Class not found in the CSV file."

        # Write all rows back to the CSV file
        with open(self.CLASS_FILE_PATH, mode="w", newline='') as file:
            csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
            csv_writer.writeheader()
            csv_writer.writerows(classes)

        return f"Member {member_id} added to class {class_id}."
