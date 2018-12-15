string = input()
dict_char = {}
for char in string:
    if char not in dict_char:
        dict_char[char] = 0
    dict_char[char] += 1
for item in dict_char:
    print(f"{item} -> {dict_char[item]}")
