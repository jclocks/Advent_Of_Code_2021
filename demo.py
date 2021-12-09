my_list = ['adcb', 'abcde', 'bce']

def char_in_string(char, stri):
    for i in stri:
        if char == i:
            return True
    return False

test_range = range(0, 3)
test_mapping = ['a', 'b', 'c', 'd', 'e']
for i in test_range:
    for j in test_mapping:
        if not char_in_string(j, my_list[i]):
            break
        good_val = my_list[i]
            

print(good_val)