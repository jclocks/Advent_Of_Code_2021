#!/usr/bin/python3

import fileinput

file_location = '/home/jtirado/Desktop/input.txt'

file_in = []
for line in fileinput.input(files=(file_location)):
    file_in.append(str(line)[0:-1])
fileinput.close()

x_pos = 0
y_pos = 0
for i in range(0, len(file_in)):
    if file_in[i].split(" ")[0] == 'up':
        y_pos -= int(file_in[i].split(" ")[1])
    if file_in[i].split(" ")[0] == 'down':
        y_pos += int(file_in[i].split(" ")[1])
    if file_in[i].split(" ")[0] == 'forward':
        x_pos += int(file_in[i].split(" ")[1])

print("Answer: " + str(x_pos * y_pos))