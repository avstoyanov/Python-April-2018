data = input()
shells = {}
while data != "Aggregate":
    reg, size = data.split()
    size = int(size)
    if reg not in shells:
        shells[reg] = []
    if size not in shells[reg]:
        shells[reg].append(size)
    data = input()

for keys in shells:
    print(keys, "->", end= "")
    first = True
    for vals in shells[keys]:
        if first:
            print(f" {vals}", end= "")
            first = False
        else:
            print(f", {vals}", end="")
    print(" (" + str(round(sum(shells[keys]) - int(sum(shells[keys])/len(shells[keys])))) + ")")
