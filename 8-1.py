#!/usr/bin/python3

import fileinput

file_location = 'inputs/8.txt'

def file_read(loc):
    file_in = []
    for line in fileinput.input(files=(loc)):
        file_in.append(str(line)[0:-1])
    fileinput.close()
    return file_in

parsed_file = file_read(file_location)
tally = 0
for line in range(len(parsed_file)):
    outputs = parsed_file[line].split(" | ")[1].split(" ")
    for i in range(len(outputs)):
        if len(outputs[i]) == 2 or len(outputs[i]) == 3 or len(outputs[i]) == 4 or len(outputs[i]) == 7:
            tally += 1
print(tally)