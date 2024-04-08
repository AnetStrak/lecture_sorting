import os

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)

    import json
    with open("sequential.json", "r") as data_file:
        data = json.load(data_file)
    for key in data.keys():
        if field == key:
            sequential_data = data [field]
            return sequential_data



    positions = []
    count []
    for 1, num in enumerate (sequence):
        if num == target:
            positions.append()
            count +=1
    return {"positions": positions, "count": count}

def main():
    pass
    sequential_data = read_data ("sequential.json", "unordered_numbers")
    print("Sequential Data:", sequential_data)

# def linear_search(sekvence, cislo):
#     return posit
#
#
#     import json
#     with open("sequential.json", "r") as file_obj:
#         allowed_keys = json.load(file_obj) ["allowed_keys"]
#
#
#     if field not in allowed_keys:
#         return None
#
#     with open(file_name, "r") as file_obj:
#         data = json.load(file_obj)
#
#     return data.get(field)
#
# def main():
#     pass
#     sequential_data = read_data ("sequential.json", "unordered_numbers")
#     print("Sequential Data:", sequential_data)
#
# def linear_search(sekvence, cislo):
#     return posit


if __name__ == '__main__':
    main()
    linear_search()