# Processing of pt HH information for AVERY labels

import csv
from datetime import date
from datetime import timedelta


HEADERS = ["name", "date", "day"]
CSV_FILE = "../RIGHT_hh.csv"


# counters
n = 0
x = 1

# Variables
pts: list = []
hh_num: int = 0
hh_size: int = 0
row: list = []
master_label: list = []


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
                row = [f'{pt} HH#{hh_num}', swab_date, series_day]
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
            row = [f"HH#{hh_num}", swabdate, series_day]
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
                row = [f"{pt} HH#{hh_num}", swabdate, series_day]
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
        row = [f"HH#{hh_num}", date_range, "Day 1 to 5"]
        master_label.append(row)

        date_range = ((date.today() + timedelta(days=6)).strftime("%m-%d") + " to "
                      + (date.today() + timedelta(days=10)).strftime("%m-%d-%y"))
        row = [f"HH#{hh_num}", date_range, "Day 6 to 10"]
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
                row = [f"{pt} HH#{hh_num}", swabdate, "Enrollment TASSO"]
                master_label.append(row)
                master_label.append(row)

                date_range = ("Between " + (date.today() + timedelta(days=30)).strftime("%m-%d") + " to " +
                              (date.today() + timedelta(days=44)).strftime("%m-%d-%y"))
                row = [f"{pt} HH#{hh_num}", date_range, "Day 30 TASSO"]
                master_label.append(row)
                master_label.append(row)

                x += 1

                if x == 2:
                    x = 1
                    break


# Start of main body
while True:
    # User input of HH information
    try:
        hh_num = int(input("What is the HH number? "))
    except ValueError as e:
        print(e)
        print("Please enter an integer.")
        continue
    hh_num =str(hh_num)


    try:
        hh_size = int(input("How many pts are in the HH? "))
    except ValueError as e:
        print(e)
        print("Please enter an integer.")
        continue


    while hh_size > n:
        try:
            if n == 0:
                pt_name = input("What is the IC's name? ")
            else:
                pt_name = input(f"What is the HC{n}'s name? ")
            if not pt_name.isalpha():
                    raise ValueError("The pt's name should not contain numbers or characters.")
            pts.append(pt_name)
            n += 1
        except ValueError as e:
            print(e)
            print("Please resubmit the pt's name.")
            continue


    # Generation of label csv
    Label_generation.label_1()
    Label_generation.label_2()
    Label_generation.label_3()
    Label_generation.label_4()
    Label_generation.label_5()


    # File storage
    try:
        with open(CSV_FILE, 'w', newline='') as file:
            write = csv.writer(file)
            write.writerow(HEADERS)
            write.writerows(master_label)
            file.close()
            print(" ")
            print('Success! CSV file can be found where script is stored.')
            print("**Remember** to deleted PHI from computer after printing, Thank you!")
    except PermissionError as e:
        print(e)
        print("Please do not have csv open while running this script.")


    break