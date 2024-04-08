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

def linear_search (sequence, target):
    positions = []
    count = []
    for i, num in enumerate (sequence):
        if num == target:
            positions.append()
            count +=1
    return {"positions": positions, "count": count}

import json
with open("sequential.json", "r") as data_file:
    data = json.load(data_file)
    sequence = data
def pattern_search(sequence, pattern):
    positions = set()
    seq_length = len(sequence)
    pattern_length = len(pattern)
    for i in range (seq_length - pattern_length + 1):
        if sequence[i:i + pattern_length] == pattern:
            positions.add((i+pattern_length)/2)
    return positions

import json
with open("sequential.json", "r") as data_file:
    data = json.load(data_file)
    for key in data.keys():
            seznam = data [ordered_numbers]

def binary_search(seznam, hledane_cislo):
    for cislo in seznam:
        if cislo == hledane_cislo:
            pozice = enumerate (seznam [:hledane_cislo])
            return pozice
        else:
            return None







def main():
    pass
    sequential_data = read_data ("sequential.json", "unordered_numbers")
    print("Sequential Data:", sequential_data)
    pattern = "ATA"

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



if __name__ == '__main__':
    main()
    target = 2 #toto se ma taky zadavat?
    linear_search (sequence, target)