raw_input = input()

replacements = [",", ";", ":", ".", "!", "(", ")", "\"", "\'", "/", "\\", "[", "]"]
for sep in replacements:
    raw_input = raw_input.replace(sep, " ")
inp_list = raw_input.split()

upper_list = []
lower_list = []
mixed_list = []

for elem in inp_list:
    if elem.isalpha():
        if elem.isupper():
            upper_list.append(elem)
        elif elem.islower():
            lower_list.append(elem)
        else:
            mixed_list.append(elem)
    else:
        mixed_list.append(elem)

print("Lower-case:", ", ".join(lower_list))
print("Mixed-case:", ", ".join(mixed_list))
print("Upper-case:", ", ".join(upper_list))
