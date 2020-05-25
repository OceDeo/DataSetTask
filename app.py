import os
import csv
import operator
import datetime
homeDir = os.environ['HOME'] 

def bottom_five_rent(): # show 5 companies with the lowest rent 
    with open(homeDir + "/Desktop/Python/DataSetTask/dataset.csv", "r") as dataset:
        sorted_list = sorted(csv.reader(dataset.readlines(), delimiter=','), key=operator.itemgetter(10), reverse=True)
    for line in sorted_list[1:6]:
        print(line)


def lease_year_25():
    lease_year_25_list = []
    total_rent = 0
    with open(homeDir + "/Desktop/Python/DataSetTask/dataset.csv", "r") as dataset:
        for line in csv.reader(dataset.readlines(), delimiter=','):
            if line[9] == '25':
                total_rent = total_rent + float(line[10])
                lease_year_25_list.append(line)
        print(lease_year_25_list)
        print(total_rent)


def masts_total_each():
    tenant_list = []
    with open(homeDir + "/Desktop/Python/DataSetTask/dataset.csv", "r") as dataset:
        for line in csv.reader(dataset.readlines()[1:], delimiter=','):
            tenant_name = line[6]
            tenant_list.append(tenant_name)
        tenant_dict = {key : tenant_list.count(key) for key in tenant_list}
        print(tenant_dict)


def main():
    bottom_five_rent()
    lease_year_25()
    masts_total_each()

if __name__ == "__main__":
    main()