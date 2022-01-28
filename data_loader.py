import csv

# this reads the csv file, and creates a list
# of the data called data_list

def read_csvfile(filename: str) -> list:
    """
    Read the csv file and return a list of the
    data from the csv file.
    """
    data = []
    with open(filename) as file:
        reader = csv.reader(file)
        next(reader)
        for line in reader:
            data.append(line)

    return data


