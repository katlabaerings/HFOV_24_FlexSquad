from Data.read_data import Data

if __name__ == '__main__':
    data = Data()
    print(f"{data.member_by_id(3).firstname} {data.member_by_id(3).lastname}")