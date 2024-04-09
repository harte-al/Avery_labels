# Processing of pt HH information for AVERY labels

import csv
from datetime import date
from datetime import timedelta

HEADERS = ["name", "date", "day"]
CSV_FILE = "RIGHT_hh.csv"

# counters
n = 0
x = 1

pts: list = []
row: list = []
master_label: list = []

# Inialize * PRESENTATION CLASSES
hh_num = input("What is the HH number?")
#TODO make this so the user inputs as int
# TODO add exception handling

hh_size = int(input("How many pts are in the HH?"))
# TODO add exception handling

while hh_size > n:
    pt_name = input("What is the pt's name?")
    # TODO add exception handling
    pts.append(pt_name)
    n += 1
print(f'pts: {pts}')

class Label_generation:
    '''

    '''
    def label_1(participants: list = pts,
                label: list = master_label):
        '''
        This function generates a list formatted for the swab bag for each pt.
        :param
        :return:updated label
        '''

        x = 1
        for pt in pts:
            while x < 11:
                swab_date = (date.today() + timedelta(days=(x - 1))).strftime("%m-%d-%y")
                series_day = "Day " + str(x)
                row = [pt, swab_date, series_day]
                master_label.append(row)
                x += 1
                if x == 11:
                    x = 1
                    break


    def label_2(label: list = master_label):
        '''
         This function generates a list formatted for the biohazard bag for the HH.
        :return:updated label
        '''
        x = 1
        while x < 11:
            swabdate = (date.today() + timedelta(days=(x - 1))).strftime("%m-%d-%y")
            series_day = "Day " + str(x)
            row = [hh_num, swabdate, series_day]
            master_label.append(row)
            x += 1


    def label_3(participants: list = pts,
                label: list = master_label):
        '''
         This function generates a list formatted for the Hologic tubes for each pt.
        :return:updated label
        '''
        x = 1
        for pt in pts:
            while x < 11:
                swabdate = (date.today() + timedelta(days=(x - 1))).strftime("%m-%d-%y")
                series_day = "Day " + str(x)
                row = [pt, swabdate, series_day]
                master_label.append(row)
                x += 1
                if x == 11:
                    x = 1
                    break


    def label_4(label: list = master_label):
        '''
         This function generates a list formatted for the Ziplock bags.
        :return:updated label
        '''
        date_range = (date.today().strftime("%m-%d") + " to "
                      + (date.today() + timedelta(days=5)).strftime("%m-%d-%y"))
        row = [hh_num, date_range, "Day 1 to 5"]
        master_label.append(row)

        date_range = ((date.today() + timedelta(days=6)).strftime("%m-%d") + " to "
                      + (date.today() + timedelta(days=10)).strftime("%m-%d-%y"))
        row = [hh_num, date_range, "Day 6 to 10"]
        master_label.append(row)


    def label_5(participants: list = pts,
                label: list = master_label):
        '''
         This function generates a list formatted for the Tasso box for each pt.
        :return:updated label
        '''
        x = 1
        for pt in pts:
            while x < 2:
                swabdate = (date.today() + timedelta(days=(x - 1))).strftime("%m-%d-%y")
                row = [pt, swabdate, "Day 1"]
                master_label.append(row)
                date_range = ("Complete between " + (date.today() + timedelta(days=30)).strftime("%m-%d-%y") + " to " +
                              (date.today() + timedelta(days=44)).strftime("%m-%d-%y"))
                row = [pt, date_range, "Day 30"]
                master_label.append(row)
                x += 1
                if x == 2:
                    x = 1
                    break
