n = int(input())
carrots = "^"*(n//2)
underscores = "_"*(n*2 - 4 - (n//2)*2)
print("/" + carrots + "\\" + underscores + "/" + carrots + "\\")
for rows in range(0,n-3):
    print("|" + " "*(2*n - 2) + "|")
print("|" + " "*(n//2 + 1) + underscores + " "*(n//2 + 1) + "|")
print("\\" + "_"*(n//2) + "/" + " "*(n*2 - 4 - (n//2)*2) + "\\" + "_"*(n//2) + "/")
