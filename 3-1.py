#!/usr/bin/python3

import fileinput

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

# For a 2D list, tally the values along the Y-axis and return a list with the results.
# Assumes the 2D list sub-lists have an equal length.
def tally_list_values(list_in):
    tally = []
    width = len(list_in[0]) + 1
    for i in range(0, width - 1):
        tally.append(int(0))
    for j in range(0, len(list_in) - 1):
        for k in range(0, width - 1):
            tally[k] += list_in[j][k]
    return tally

# Alright I'm officially hating this one now screw this
def gamma(tally, length):
    result = []
    for i in range(0, len(tally)):
        if tally[i] > (length / 2):
            result.append(1)
        else:
            result.append(0)
    return result

# Seriously wtf
def epsilon(tally, length):
    result = []
    for i in range(0, len(tally)):
        if tally[i] > (length / 2):
            result.append(0)
        else:
            result.append(1)
    return result

# arrrrrrgh I had to fine tune these functions like 10 times
def item_to_decimal(list_in):
    result = ""
    for i in range(0, len(list_in)):
        result += str(list_in[i])
    return int('0b' + result, 2)

input_list = file_to_2D_list('/home/jtirado/Desktop/input.txt')
gamma_val = gamma(tally_list_values(input_list), len(input_list))
epsilon_val = epsilon(tally_list_values(input_list), len(input_list))
print("Answer: " + str(item_to_decimal(gamma_val) * item_to_decimal(epsilon_val)))