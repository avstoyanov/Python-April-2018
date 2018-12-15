stock = {}
raw = ""
key = ""
val = ""
switch = 0
while raw != "exam time":
    if raw != "shopping time" and switch == 0:
        if raw != "":
            data = raw.split(" ")
            key = data[1]
            val = data[2]
            if key not in stock:
                stock[key] = 0
            stock[key] += int(val)
        raw = input()
    else:
        switch = 1
        if raw != "shopping time":
            data = raw.split(" ")
            key = data[1]
            val = data[2]
            if key in stock:
                if stock[key] <= 0:
                    print(f"{key} out of stock")
                else:
                    stock[key] -= int(val)
            else:
                print(f"{key} doesn't exist")

        raw = input()
for item in stock:
    if stock[item] > 0:
        print(f"{item} -> {stock[item]}")
