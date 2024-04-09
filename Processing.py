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


# label 4
date_range = date.today().strftime("%m-%d-%y") + " to " + (date.today() + timedelta(days=5)).strftime("%m-%d-%y")
row1 = [hh_num, date_range, "Day 1 to 5"]
date_range = (date.today() + timedelta(days=6)).strftime("%m-%d-%y") + " to " + (date.today() + timedelta(days=10)).strftime("%m-%d-%y")
row2 = [hh_num, date_range, "Day 6 to 10"]

label4.append(row1)
label4.append(row2)
print(f"label4 : {label4}")

# label 5
for pt in pts:
    while x < 2:
        swabdate = (date.today() + timedelta(days=(x - 1))).strftime("%m-%d-%y")
        row1 = [pt, swabdate, "Day 1"]
        label5.append(row1)
        date_range = ("Complete between " + (date.today() + timedelta(days=30)).strftime("%m-%d-%y") + " to " +
                      (date.today() + timedelta(days=44)).strftime("%m-%d-%y"))
        row2 = [pt, date_range, "Day 30"]
        label5.append(row2)
        x += 1
        if x == 2:
            x = 1
            break
print(f"Label5 : {label5}")

master_label.append(label1)
master_label.append(label2)
master_label.append(label3)
master_label.append(label4)
master_label.append(label5)

print(f"master_label: {master_label}")

with open(CSV_FILE, 'w') as file:
    write = csv.writer(file)

    write.writerow(HEADERS)
    write.writerows(master_label)
file.close()
