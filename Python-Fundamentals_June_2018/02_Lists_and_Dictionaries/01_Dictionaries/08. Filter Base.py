age = {}
salary = {}
position = {}
raw = ""
while raw != "filter base":
    if raw != "":
        key, val = raw.split(" -> ")
        try:
            val = float(val)
        except ValueError:
            val = val #placeholder to midigate syntax error
        if isinstance(val, float) and val%1 == 0:
            age[key] = int(val)
        elif isinstance(val, float):
            salary[key] = val
        else:
            position[key] = val
    raw = input()
raw = input()
if raw == "Age":
    for item in age:
        print(f"Name: {item}")
        print(f"Age: {age[item]}")
        print("====================")
elif raw == "Salary":
    for item in salary:
        print(f"Name: {item}")
        print(f"Salary: {salary[item]}")
        print("====================")
else:
    for item in position:
        print(f"Name: {item}")
        print(f"Position: {position[item]}")
        print("====================")
