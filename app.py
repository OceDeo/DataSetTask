import os
import csv
import operator
from datetime import datetime
from datetime import date

homeDir = os.environ['HOME'] 

USER_OPTIONS = """
    - 1 - Show tenants with lowest rent
    - 2 - Show tenants with 25 year lease
    - 3 - Show tenants and how many masts they rent
    - 4 - Show tenants rented the masts between 01/06/1999 - 30/08/2007
    - 5 - Show all the information above
    - q - quit
    Enter: """


def bottom_five_rent(): 
    with open(homeDir + "/Desktop/Python/DataSetTask/dataset.csv", "r") as dataset:
        sorted_list = sorted(csv.reader(dataset.readlines()[1:6], delimiter=','), key=operator.itemgetter(10), reverse=True)
    return sorted_list


def lease_year_25():
    lease_yr25 = []
    t_rent = 0
    with open(homeDir + "/Desktop/Python/DataSetTask/dataset.csv", "r") as dataset:
        for line in csv.reader(dataset.readlines(), delimiter=','):
            if line[9] == '25':
                t_rent = t_rent + float(line[10])
                lease_yr25.append(line)
        return t_rent, lease_yr25


def masts_total_each():
    t_l = []
    with open(homeDir + "/Desktop/Python/DataSetTask/dataset.csv", "r") as dataset:
        for line in csv.reader(dataset.readlines()[1:], delimiter=','):
            t_n = line[6]
            t_l.append(t_n)
            tenant_dict = {key : t_l.count(key) for key in t_l}
        return tenant_dict


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
        return lease_in_dates_list


def menu():
    user_input = input(USER_OPTIONS)
    while user_input != 'q':
        if user_input == '1':
            print(bottom_five_rent())
        elif user_input == '2':
            print(lease_year_25())
        elif user_input == '3':
            print(masts_total_each())
        elif user_input == '4':
            print(lease_in_date())
        elif user_input == '5':
            print(bottom_five_rent())
            print(lease_year_25())
            print(masts_total_each())
            print(lease_in_date())
        elif user_input == 'q':
            exit()
        else:
            print("Unexpected input, try again")
        user_input = input(USER_OPTIONS)
        
            
def main():
    menu()

if __name__ == "__main__":
    main()
