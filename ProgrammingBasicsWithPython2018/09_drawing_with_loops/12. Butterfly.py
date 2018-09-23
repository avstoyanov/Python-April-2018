n = int(input()) - 2
for top in range(0, n):
    if top % 2 == 0:
        print("*"*n + "\\" + " " + "/" + "*"*n)
    else:
        print("-" * n + "\\" + " " + "/" + "-" * n)
print(" "*(n+1) + "@")
for bottom in range(0, n):
    if bottom % 2 == 0:
        print("*"*n + "/" + " " + "\\" + "*"*n)
    else:
        print("-" * n + "/" + " " + "\\" + "-" * n)
