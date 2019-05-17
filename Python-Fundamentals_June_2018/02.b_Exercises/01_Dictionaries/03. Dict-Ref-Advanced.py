names = {}
raw_input = input()
while raw_input != "end":
    name, val = raw_input.split(" -> ")
    if val.isalpha():
        if val in names:
            if name in names:
                names[name] = names[name] + ", " + names[val]
            else:
                names[name] = names[val]
    else:
        if name in names:
            names[name] = names[name] + ", " + val
        else:
            names[name] = val
    raw_input = input()
for element in names:
    print(f"{element} === {names[element]}")
