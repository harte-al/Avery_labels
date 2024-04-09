# Processing of pt HH information for AVERY labels

import csv
from datetime import date
from datetime import timedelta


HEADERS = ["name", "date", "day"]
CSV_FILE = "RIGHT_hh.csv"


# counters
n = 0
x = 1

pts = []
row = []
label1 = [] #TODO make all of the labels just append to master label
label2 = []
label3 = []
label4 = []
label5 = []
label6 = []
master_label = []


# Inialize *UI CLASSES 
hh_num = input("What is the HH number?")
# TODO make this so the user inputs as int
# TODO add exception handling

hh_size = int(input("How many pts are in the HH?"))
# TODO add exception handling

while hh_size > n:
    pt_name = input("What is the pt's name?")
    # TODO add exception handling
    pts.append(pt_name)
    n += 1
print(f'pts: {pts}')


# label 1
for pt in pts:
    while x < 11:
        swabdate = (date.today() + timedelta(days=(x - 1))).strftime("%m-%d-%y")
        series_day = "Day " + str(x)
        row = [pt, swabdate, series_day]
        label1.append(row)
        x += 1
        if x == 11:
            x = 1
            break
print(f"Label1 : {label1}")

# label 2
row = []
while x < 11:
    swabdate = (date.today() + timedelta(days=(x - 1))).strftime("%m-%d-%y")
    series_day = "Day " + str(x)
    row = [hh_num, swabdate, series_day]
    label2.append(row)
    x += 1
print(f"Label2 : {label2}")
x = 1

# label 3
row = []
for pt in pts:
    while x < 11:
        swabdate = (date.today() + timedelta(days=(x - 1))).strftime("%m-%d-%y")
        series_day = "Day " + str(x)
        row = [pt, swabdate, series_day]
        label3.append(row)
        x += 1
        if x == 11:
            x = 1
            break
print(f"Label3 : {label3}")
