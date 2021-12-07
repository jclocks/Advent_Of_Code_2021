#!/usr/bin/python3

import fileinput
import scipy
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

def item_to_decimal(list_in):
    result = ""
    for i in range(0, len(list_in)):
        result += str(list_in[i])
    return int('0b' + result, 2)

def most_common_value(list_in, column):
    items = []
    for i in list_in[column]:
        items.append(i)
    return scipy.stats.mode(items)[0][0]

o2_list_in = file_to_2D_list('/home/jtirado/Desktop/input.txt')
co2_list_in = file_to_2D_list('/home/jtirado/Desktop/input.txt')
o2_list = []
co2_list = []

for column in range(0, 12):
    mcv = most_common_value(o2_list_in, column)
    print("MCV: " + str(mcv))
    for sublist in range(0, len(o2_list_in) - 1):
        if o2_list_in[sublist][column] != mcv:
            o2_list_in.remove(sublist)
    print(len(o2_list_in))



print(len(o2_list_in))