n = int(input())
print("."*(n+1) + "_"*(2*n + 1) + "."*(n+1))
for top in range(0, n):
    print("."*(n - top) + "//" + "_"*(2 * n - 1 + 2*top) + "\\\\" + "."*(n - top))
print("//" + "_"*((2 * n - 1 + 2*n)//2 - 2) + "STOP!" + "_"*((2 * n - 1 + 2*n)//2 - 2) + "\\\\")
for bottom in range(0, n):
    print("."*bottom + "\\\\" + "_"*(2 * n - 1 + 2*(n-bottom)) + "//" + "."*bottom)
