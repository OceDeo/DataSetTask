import os
import csv
import operator
from datetime import datetime
from datetime import date

homeDir = os.environ['HOME'] 
"""
date = "19 Aug 2009"
datetime_obj = datetime.strptime(date,'%d %b %Y')
print(type(datetime_obj))
print(datetime_obj)
"""

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


def lease_in_date():
    lease_in_dates_list = []
    with open(homeDir + "/Desktop/Python/DataSetTask/dataset.csv", "r") as dataset:
        for line in csv.reader(dataset.readlines()[1:], delimiter=','):
            datetime_obj = datetime.strptime(line[7],'%d %b %Y').date()
            initial_date = date(1999, 6, 1)
            final_date = date(2007, 8, 30)
            if datetime_obj >= initial_date and datetime_obj <= final_date:
                datetime_obj_fin = datetime.strptime(line[8],'%d %b %Y').date()
                line[7] = str(datetime_obj.strftime('%d/%m/%Y'))
                line[8] = str(datetime_obj_fin.strftime('%d/%m/%Y'))
                lease_in_dates_list.append(line)
        print(lease_in_dates_list)


def main():
    bottom_five_rent()
    lease_year_25()
    masts_total_each()

if __name__ == "__main__":
    main()