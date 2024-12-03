import csv

def main():
    print("halló")
    print_class_by_id("../Data/class_data.csv",1)


def print_class_by_id(file_path, target_id):
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if row['id'] == str(target_id):  # Compare as string
                print(row)
                print(row['class'])  # Print the 'class' column

if __name__ == "__main__":
    main()

