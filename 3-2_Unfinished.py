#!/usr/bin/python3

import fileinput, scipy
from scipy.stats import mode

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

file_loc = '/home/jtirado/Desktop/input.txt'
file_read = file_to_2D_list(file_loc)
width = len(file_read[0])
height = len(file_read)
o2_list, co2_list = file_read, file_read

def math_mode(list_in):
    return scipy.stats.mode(list_in)[0][0]

def most_common_value(list_in, column):
    values = []
    for i in list_in[column]:
        values.append(i)
    return math_mode(values)

def item_to_decimal(list_in):
    result = ""
    for i in range(0, len(list_in)):
        result += str(list_in[i])
    return int('0b' + result, 2)

for x in range(0, len(o2_list[0]) - 1):
    new_o2_list = []
    for y in range(0, len(o2_list) - 1):
        mcv = most_common_value(o2_list, y)
        if o2_list[y][x] == mcv:
            new_o2_list.append(o2_list[y])
    o2_list = new_o2_list
    if len(o2_list) <= 1:
        break

for x in range(0, len(co2_list[0]) - 1):
    new_co2_list = []
    for y in range(0, len(co2_list) - 1):
        mcv = most_common_value(co2_list, y)
        if co2_list[y][x] != mcv:
            new_co2_list.append(co2_list[y])
    co2_list = new_co2_list
    if len(co2_list) <= 1:
        break

print('Answer: ' + str(item_to_decimal(o2_list[0]) * item_to_decimal(co2_list[0])))