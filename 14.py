# 14. Write a function that reads a CSV file. It should return a list of
# dictionaries, using the first row as key names, and each subsequent
# row as values for those keys.

import csv

def readCSV(filename):
    with open(filename,mode='r') as sample1:
        read_file = csv.DictReader(sample1)

        with open ('new.csv',mode='w') as new:
            write_file = csv.writer(new)
            sample_dict = { row[0] : row[1] for row in read_file }
        print(sample_dict)

readCSV("sample.csv")