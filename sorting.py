import os #co to je???
import csv

def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, "r") as csv_file:
        reader = csv.DictReader(csv_file) #interesting
        data = {}
        for row in reader:
            for header, value in row.items():
                if header not in data:
                    data[header].append[int(value)]
                else:
                    data[reader].append(int(value))
            print(row)
    return data

#prohayuje nejmensi prvek s aktualnim, najivn9 algoritmus
#DictReader da uz vypsane

def selection_sort(data):
    # my_list[1], my_list[3] = my_list[3], my_list[1]
    #vysledky = {}
    #for my_list in data
    #     vysledek = []
    #     for jednotka in my_list:
    #         nejmensi = min(jednotka)
    #         for
    #             if
    #                 my_list[1], my_list[3] = my_list[3], my_list[1]
    #         vysledek = jednotka.append
    #     vysledky = vysledek.append()
    # return vysledky

def selection_sort(data):
    for jednotka in my_list:
        nejmensi = min(jednotka)
        for
            if
                my_list[1], my_list[3] = my_list[3], my_list[1]
        vysledek = jednotka.append
    vysledky = vysledek.append()
    return vysledky


def main():
    pass
    final = selection_sort(read_data("numbers.csv"))
    return final

if __name__ == '__main__':
    main()
