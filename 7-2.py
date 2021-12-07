import fileinput

def file_to_list(file_location):
    file_in = []
    for line in fileinput.input(files=(file_location)):
        file_in = str(line)[0:-1].split(',')
    fileinput.close()
    for i in range(0, len(file_in)):
        file_in[i] = int(file_in[i])
    return file_in

input_file = file_to_list('/home/jtirado/input-7.txt')

possible_solutions = {}
for i in range(min(input_file), max(input_file)):
    total_abs = 0
    for j in input_file:
        total_abs += sum(range(1, abs(j - i) + 1))
        possible_solutions[i] = total_abs

print('Answer: ' + str(possible_solutions[min(possible_solutions, key=possible_solutions.get)]))