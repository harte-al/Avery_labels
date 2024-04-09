
n = 0
pts: list = []

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