n = int(input())
def square(n):
    print(2*n*"-")
    for rows in range(1, n-1):
        print("-"+"\\/"*(n-1) + "-")
    print(2*n*"-")
square(n)
