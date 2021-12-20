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

# Retrieves a list of values of neighboring cells.
def retrieve_neighbors(list_in, x, y):
    results = []
	# North
    if y - 1 == -1:
        results.append(9)
    else:
        results.append(list_in[y - 1][x])
		
	# South
    if y + 1 == len(list_in):
        results.append(9)
    else:
        results.append(list_in[y + 1][x])
	# East
    if x == len(list_in[0]) - 1:
        results.append(9)
    else:
        results.append(list_in[y][x + 1])
	# West            
    if x == 0:
        results.append(9)
    else:
        results.append(list_in[y][x - 1])
    return results

new_id = 10
for i in range(30):
    for y in range(len(file_in)):
        for x in range(len(file_in[0])):
            if file_in[y][x] == 9:
                pass
            else:
                if max(retrieve_neighbors(file_in, x, y)) <= 9:
                    new_id += 1
                    file_in[y][x] = new_id
                if max(retrieve_neighbors(file_in, x, y)) > 9:
                    compare = list(filter(lambda a: a != 9, retrieve_neighbors(file_in, x, y)))
                    file_in[y][x] = max(compare)

flat_in = []
for y in range(len(file_in)):
    for x in range(len(file_in[0])):
        flat_in.append(file_in[y][x])

results = {}
for i in flat_in:
    if i not in results:
        results[i] = 1
    else:
        results[i] += 1

print({k: v for k, v in sorted(results.items(), key=lambda item: item[1])})