import os
import csv
import operator
homeDir = os.environ['HOME'] 


def bottom_five_rent():
    with open(homeDir + "/Desktop/Python/DataSetTask/dataset.csv", "r") as dataset:
        sorted_list = sorted(csv.reader(dataset.readlines(), delimiter=','), key=operator.itemgetter(10), reverse=True)
    for line in sorted_list[1:6]:
        print(line)


