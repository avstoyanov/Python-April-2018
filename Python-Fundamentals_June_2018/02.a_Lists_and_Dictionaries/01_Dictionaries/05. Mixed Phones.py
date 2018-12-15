phonebook = {}
raw = ""
key = ""
val = ""
while raw != "Over":
    if raw != "":
        dataset = raw.split(" : ")
        key = dataset[0]
        val = dataset[1]
        if key.isnumeric():
            tmp = key
            key = val
            val = tmp
        phonebook[key] = val
    raw = input()
sortbook = sorted(phonebook)
for item in sortbook:
    print(f"{item} -> {phonebook[item]}")
