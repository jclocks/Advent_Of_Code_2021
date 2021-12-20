#!/usr/bin/python3

import fileinput

file_location = 'inputs/9.txt'

def file_read(loc):
    file_in = []
    for line in fileinput.input(files=(loc)):
        file_in.append(str(line)[0:-1])
    fileinput.close()
    return file_in

# Read the file and format it into a 2D List.
file_in = file_read(file_location)
for i in range(len(file_in)):
    file_in[i] = list(file_in[i])

# Convert 2D list of strings to integers
for row in range(len(file_in)):
    file_in[row] = list(map(int, file_in[row]))

# First rollercoaster drop: Retrieve the low points.
# Function assumes list is rectangle (every x-length is the same.)
def retrieve_low_points(list_2d_in):
    results = []
    for y in range(len(list_2d_in)):
        for x in range(len(list_2d_in[0])):
            try:
                north = list_2d_in[y - 1][x]
            except IndexError:
                north = 9
            try:
                south = list_2d_in[y + 1][x]
            except IndexError:
                south = 9
            if x == len(list_2d_in[0]) - 1:
                east = 9
            else:
                east = list_2d_in[y][x + 1]                
            if x == 0:
                west = 9
            else:
                west = list_2d_in[y][x - 1] 
            if list_2d_in[y][x] < north and list_2d_in[y][x] < south and list_2d_in[y][x] < east and list_2d_in[y][x] < west:
                results.append(list_2d_in[y][x])
    return results

answer = sum(retrieve_low_points(file_in)) + len(retrieve_low_points(file_in))
print(answer)
