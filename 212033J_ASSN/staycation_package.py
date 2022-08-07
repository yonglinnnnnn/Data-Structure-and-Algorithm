# Name: Xu Yong Lin
# Admin no: 212033J
# Tutorial group: IT2153-01

import time

from search import *
from sort import *


class StaycationPackage:
    def __init__(self, packageName, customerName, pax, packageCost):
        self.packagename = packageName.upper()
        self.customername = customerName.upper()
        self.totalpax = pax
        self.packagecost = packageCost
        self.totalcost = 0

    def total_cost(self):
        self.totalcost = (self.packagecost * self.totalpax)
        return self.totalcost


class colors:
    RED = '\033[91m'
    MAGENTA = '\033[95m'
    BLUE = '\033[94m'
    RESET = '\033[0m'


records = [StaycationPackage('Crowne Plaza', 'Ruri', 4, 248),
           StaycationPackage('Holiday Inn', 'Clara', 3, 351),
           StaycationPackage('Happy Holiday', 'Rachel', 4, 349),
           StaycationPackage('Polli Manifest', 'Tom', 4, 225),
           StaycationPackage('Happy Holiday', 'Kylia', 4, 175),
           StaycationPackage('Kings Holiday', 'Vivi', 2, 100),
           StaycationPackage('Sentosa Island', 'Clara', 4, 250),
           StaycationPackage('Dandy Package', 'Simon', 3, 150),
           StaycationPackage('Jijuko Place', 'John', 5, 250),
           StaycationPackage('Popisto Hotel', 'Samuel', 2, 500)]


def update(l):
    record = records[l]
    while True:
        try:
            print(
                f'Changing record for {records[l].packagename}, {records[l].customername}, {record.totalpax}, {record.packagecost} \n'
                '1. Package Name\n'
                '2. Customer Name\n'
                '3. Total Number of Pax\n'
                '4. Package cost per Pax\n'
                '-1. Exit back to inventory')

            usr_input = input('Enter what you want to change (1-4, or -1): ')
            if usr_input == '1':
                while True:
                    pname = input('New Package Name: ')
                    if pname.replace(" ", "").isalpha():
                        records[l].packagename = pname.upper()
                        print(f'Package Name has been changed to {records[l].packagename}')
                        break
                    else:
                        print('Package name can only contain letters!')
                        continue
                continue
            elif usr_input == '2':
                while True:
                    cname = input('New Customer Name: ')
                    if cname.replace(" ", "").isalpha():
                        record.customername = cname.upper()
                        print(f'Customer Name has been changed to {record.customername}')
                        break
                    else:
                        print(f'Customer name can only contain letters!')
                continue
            elif usr_input == '3':
                newpax = int(input('New Total Number of Pax: '))
                if newpax >= 1:
                    record.totalpax = newpax
                    print(f'Total Number of Pax has been changed to {record.totalpax}')
                else:
                    print(f"No. of Pax must at least be 1")
                continue
            elif usr_input == '4':
                costperpax = float(input('New Package cost per pax: '))
                if costperpax > 0:
                    record.packagecost = costperpax
                    print(f'Package cost per pax has been changed to {record.packagecost}')
                else:
                    print("New package cost must at least be 0")
                continue
            elif usr_input == '-1':
                break
            else:
                print('Please enter a valid number. ')
            break
        except Exception as e:
            print(f'Please enter a valid input ({e})')


def display(lists):
    print(f'      PckgName        CustName    NoOfPax     PckgCost    TotalCost')
    if len(lists) > 0:
        for c in range(0, len(lists)):
            print(
                f'{c + 1}.\t {lists[c].packagename}\t\t {lists[c].customername}\t\t {lists[c].totalpax}\t\t   {lists[c].packagecost :.2f}\t\t {lists[c].total_cost() :.2f}')
            time.sleep(0.5)
        print()
    else:
        print('Nothing is found!')


def check(l):
    while True:
        try:
            if len(l) > 1:
                # try:
                choice = int(input('Choose a number to change the output: '))
                choice -= 1
                if choice > len(l) or choice < 0:
                    print('Enter a valid number!')
                    continue
                else:
                    for i in range(len(records) - 1):
                        if l[choice] == records[i]:
                            # record = records[i]
                            update(i)
                            break
                # break
            else:
                for i in range(len(records)):
                    # if ip == 0:
                    if records[i] == l[0]:
                        update(i)
            break
        except TypeError:
            print('Please enter a valid number!')
        except Exception as e:
            print(f'Error occured. ({e})')
            break


def price_range(l, lowbound, upbound):
    filtered = []
    for i in range(len(l)):
        if l[i].packagecost <= upbound and l[i].packagecost >= lowbound:
            filtered.append(l[i])
    filtered.sort(key=lambda x: x.packagecost)
    return filtered


while True:
    try:
        print(f'=== Staycation Package Deals Inventory === \n'
              f'1. Display all records \n'
              f'{colors.MAGENTA}2. Sort record by Customer Name using Bubble sort \n'
              f'3. Sort record by Package Name using Selection sort \n'
              f'4. Sort record by Package Cost using Insertion sort {colors.RESET} \n'
              f'{colors.BLUE}5. Search record by Customer Name using Linear Search and update record \n'
              f'6. Search record by Package Name using Binary Search and update record {colors.RESET} \n'
              f'{colors.RED}7. List records range from $X to $Y ($100 - $200) {colors.RESET} \n'
              f'{colors.MAGENTA}8. Sort records by Total Cost using Radix sort\n'
              f'9. Sort records by Package Cost using Heap Sort {colors.RESET}\n'
              f'{colors.BLUE}10. Search record by No. of Pax using Interpolation Search and update record {colors.RESET} \n'
              f'0. Exit Application')
        user_input = input('Choose a number (0-10): ')
        # display all records
        if user_input == '1':
            print('Displaying all records')
            display(records)
        # bubble sort customer name
        elif user_input == '2':
            records = bubble_sort(records)
        # sort record by package name using selection sort
        elif user_input == '3':
            records = selection_sort(records)
        # sort record by package cost using insertion sort
        elif user_input == '4':
            records = insertion_sort(records)
        # 5. linear search customer name
        elif user_input == '5':
            n = input('Enter Customer Name: ')
            output = linearSearch(records, len(records), n)
            lists = []
            for i in output:
                lists.append(records[i])
            display(lists)
            check(lists)
        # 6. Binary Search package name
        elif user_input == '6':
            n = input('Enter Package Name: ')
            records.sort(key=lambda x: x.packagename)
            output = binarySearch(records, n)
            lists = []
            for i in output:
                lists.append(records[i])
            display(lists)
            check(lists)
        # list records range from $X to $Y
        elif user_input == '7':
            print('List records range from $X to $Y')
            up_bound = 0
            low_bound = 0
            while 1:
                try:
                    low_bound = float(input('Enter lower bound ($X): '))
                    up_bound = float(input('Enter upper bound ($Y): '))
                    if low_bound > 0 and up_bound > low_bound:
                        k = price_range(records, low_bound, up_bound)
                        display(k)
                        break
                    else:
                        print("Error occured. Please try again")
                except ValueError:
                    print('Please enter a correct number! ')
                    continue
        # 8. radix sort
        elif user_input == '8':
            print('Sort record by Package Cost using Radix sort')
            output = radixSort(records)
        # 9. heap sort
        elif user_input == '9':
            print('Sort record by Total Cost using Heap Sort')
            heapSort(records)
        # 10. Interpolation Search
        elif user_input == '10':
            print('Search record by No. Of Pax using Interpolation Search')
            n = int(input('Enter No. Of Pax: '))
            records.sort(key=lambda x: x.totalpax)
            output = interpolationSearch(records, len(records), n)
            lists = []
            for i in output:
                lists.append(records[i])
            display(lists)
            check(lists)
        elif user_input == '0':
            print('Thank you! Application ends here.')
            break
        else:
            print('Number chosen is out of range. Choose a number (0-10): ')

    # error handling
    except EOFError:
        print('Thank you! Application ends here')
        break
    # except Exception as e:
    #     print(f'Error occured ({e})')
    #     continue
