import fileinput

def file_to_list(file_location):
    file_in = []
    for line in fileinput.input(files=(file_location)):
        file_in = str(line)[0:-1].split(',')
    fileinput.close()
    for i in range(0, len(file_in)):
        file_in[i] = int(file_in[i])
    return file_in

input_file = file_to_list('/home/jtirado/input-6-practice.txt')
days = 256

for i in range(days):
    for fish in range(0, len(input_file)):
        if input_file[fish] == 0:
            input_file[fish] = 6
            input_file.append(8)
        else:
            input_file[fish] -= 1

print(len(input_file))
