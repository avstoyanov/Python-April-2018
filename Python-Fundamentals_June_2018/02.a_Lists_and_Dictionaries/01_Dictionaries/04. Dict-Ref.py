raw = input()
key = ""
val = 0
dict_stuff = {}
while raw != "end":
    keyval = raw.split(" = ")
    key = keyval[0]
    val = keyval[1]
    if val not in dict_stuff and val.isnumeric() == True:
        dict_stuff[key] = int(val)
    else:
        if val in dict_stuff:
            dict_stuff[key] = dict_stuff[val]

    raw = input()
for item in dict_stuff:
    print(f"{item} === {dict_stuff[item]}")
