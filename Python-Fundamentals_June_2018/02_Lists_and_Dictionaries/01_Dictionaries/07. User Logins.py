users = {}
raw = ""
login = False
counter = 0
while raw != "end":
    if raw != "login" and login == False:
        if raw != "":
            key, val = raw.split(" -> ")
            users[key] = val
        raw = input()
    else:
        login = True
        if raw != "login":
            key, val = raw.split(" -> ")
            if key not in users:
                print(f"{key}: login failed")
                counter += 1
            elif users[key] != val:
                print(f"{key}: login failed")
                counter += 1
            else:
                print(f"{key}: logged in successfully")
        raw = input()
print(f"unsuccessful login attempts: {counter}")
