#!/usr/bin/python3

import fileinput, scipy
from statistics import multimode

# Makes a 2D list out of the supplied file.
# Ex. file with contents "100\n101" returns:
# [ [ 1, 0, 0 ],
#   [ 1, 0, 1 ] ]
def file_to_2D_list(file_location):
    file_in = []
    for line in fileinput.input(files=(file_location)):
        file_in.append(list(map(int, str(line)[0:-1])))
    fileinput.close()
    return file_in

file_loc = 'inputs/3.txt'
file_read = file_to_2D_list(file_loc)
width = len(file_read[0])
height = len(file_read)
o2_list, co2_list = file_read, file_read

def most_common_value(list_in, column):
    values = []
    for i in range(len(list_in)):
        values.append(list_in[i][column])
    if multimode(values) == [0, 1] or multimode(values) == [1, 0]:
        return 1
    else:
        return multimode(values)[0]

def item_to_decimal(list_in):
    result = ""
    for i in range(0, len(list_in)):
        result += str(list_in[i])
    return int('0b' + result, 2)

for x in range(0, len(o2_list[0])):
    new_o2_list = []
    for y in range(0, len(o2_list)):
        mcv = most_common_value(o2_list, x)
        if o2_list[y][x] == mcv:
            new_o2_list.append(o2_list[y])
    o2_list = new_o2_list
    if len(o2_list) <= 1:
        break

for x in range(0, len(co2_list[0])):
    new_co2_list = []
    for y in range(0, len(co2_list)):
        mcv = most_common_value(co2_list, x)
        if co2_list[y][x] != mcv:
            new_co2_list.append(co2_list[y])
    if new_co2_list == []:
        new_co2_list = co2_list
    co2_list = new_co2_list
    if len(co2_list) <= 1:
        break

o2 = item_to_decimal(o2_list[0])
co2 = item_to_decimal(co2_list[0])
print('Answer: ' + str(o2 * co2))
