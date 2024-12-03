import pandas as pd

manager_data = "../Data/manager_data.csv"
member_data = "../Data/member_data.csv"

managers = pd.read_csv(manager_data)
members = pd.read_csv(member_data)

print("\nManagers:")
print(managers.to_string())
print("\nMembers:")
print(members.to_string())
