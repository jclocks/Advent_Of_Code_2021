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

left_list = parsed_file[0].split(" | ")[0].split(" ")

mapping = {}
bd_pool = []
dg_pool = []

"""
FYI, using a specific scheme for the number displays:

 aaaa
b    c
b    c
 dddd
e    f
e    f
 gggg

"""
# Determine letters comprising 8 and 1
for i in range(len(left_list)):
  if len(left_list[i]) == 7:
    mapping['out8'] = left_list[i]
  if len(left_list[i]) == 2:
    mapping['out1'] = left_list[i]

# Determine letters comprising 7, and what's mapped to A.
for i in range(len(left_list)):
  if len(left_list[i]) == 3:
    mapping['out7'] = left_list[i]
    for j in list(mapping['out7']):
      if j not in list(mapping['out1']):
        mapping['posA'] = j

# Determine letters comprising 4, and what's mapped to either B or D.
for i in range(len(left_list)):
    if len(left_list[i]) == 4:
        mapping['out4'] = left_list[i]
        for j in list(mapping['out4']):
            if j not in list(mapping['out1']):
                bd_pool.append(j)

# Determine letters comprising 5, and what's mapped to either D or G.
for i in range(len(left_list)):
    if len(left_list[i]) == 5:
        for j in list(mapping['out1']):
            if j not in list(left_list[i]):
                break
        mapping['out5'] = left_list[i]

for i in list(mapping['out5']):
    if i not in list(mapping['out7']):
        dg_pool.append(i)

# Determine what's mapped to B and D.
if bd_pool[0] in dg_pool:
    mapping['posD'] = bd_pool[0]
    mapping['posB'] = bd_pool[1]
else:
    mapping['posD'] = bd_pool[1]
    mapping['posB'] = bd_pool[0]

# Determine letters comprising 9, and what's mapped to G.
for i in range(len(left_list)):
	if len(left_list[i]) == 6 and mapping['posA'] in list(left_list[i]) and mapping['posB'] in list(left_list[i]) and mapping['posD'] in list(left_list[i]):
		mapping['out9'] = left_list[i]

for i in list(mapping['out9']):
	if i not in list(mapping['out5']):
		mapping['posG'] = i

# Determine letters comprising 5, and what's mapped to F.
for i in range(len(left_list)):
	if len(left_list[i]) == 5 and mapping['posA'] in list(left_list[i]) and mapping['posB'] in list(left_list[i]) and mapping['posD'] in list(left_list[i]) and mapping['posG'] in list(left_list[i]):
		mapping['out5'] = left_list[i]

for i in list(mapping['out5']):
	if i not in [mapping['posA'], mapping['posB'], mapping['posD'], mapping['posG']]:
		mapping['posF'] = i

# Determine what's mapped to C.
for i in list(mapping['out4']):
	if i not in [mapping['posB'], mapping['posD'], mapping['posF']]:
		mapping['posC'] = i

# Determine what's mapped to E. We now have a full map for letters.
for i in list('abcdefg'):
	if i not in [mapping['posA'], mapping['posB'], mapping['posC'], mapping['posD'], mapping['posF'], mapping['posG']]:
		mapping['posE'] = i

# Determine letters comprising 2.
for i in range(len(left_list)):
    for j in [mapping['posA'], mapping['posC'], mapping['posD'], mapping['posE'], mapping['posG']]:
        if j not in list(left_list[i]):
            break
    mapping['out2'] = left_list[i]

# Determine letters comprising 0.
for i in range(len(left_list)):
    for j in [mapping['posA'], mapping['posB'], mapping['posC'], mapping['posE'], mapping['posF'], mapping['posG']]:
        if j not in list(left_list[i]):
            break
    mapping['out0'] = left_list[i]

print(mapping)