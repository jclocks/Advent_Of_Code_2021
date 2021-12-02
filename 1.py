#!/usr/bin/python3

import fileinput

file_location = '/home/jtirado/Desktop/input.txt'

file_in = []
for line in fileinput.input(files=(file_location)):
    file_in.append(int(line))
fileinput.close()

answer = 0
for i in range(1, len(file_in)):
    if file_in[i] > file_in[i - 1]:
        answer += 1

print("Answer: " + str(answer))
