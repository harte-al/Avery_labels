import csv
from processing import Label_generation

HEADERS = ["name", "date", "day"]
CSV_FILE = "RIGHT_hh.csv"

master_label: list = []
pts: list = []

Label_generation.label_1()
Label_generation.label_2()
Label_generation.label_3()
Label_generation.label_4()
Label_generation.label_5()

# File storage
with open(CSV_FILE, 'w', newline='') as file:
    write = csv.writer(file)
    write.writerow(HEADERS)
    write.writerows(master_label)
file.close()
