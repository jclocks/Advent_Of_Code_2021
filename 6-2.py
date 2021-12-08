import fileinput

def file_to_list(file_location):
    file_in = []
    for line in fileinput.input(files=(file_location)):
        file_in = str(line)[0:-1].split(',')
    fileinput.close()
    for i in range(0, len(file_in)):
        file_in[i] = int(file_in[i])
    return file_in

input_file = file_to_list('inputs/6.txt')
days = 256

fish_horde = {}
for i in range(9):
    fish_horde[i] = 0

for i in input_file:
    fish_horde[i] += 1

for i in range(days):
    spawn = fish_horde[0]
    for j in range(8):
        fish_horde[j] = fish_horde[j + 1]
    fish_horde[6] += spawn
    fish_horde[8] = spawn

total = 0
for i in range(9):
    total += fish_horde[i]

print('Answer: ' + str(total))