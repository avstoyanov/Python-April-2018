n = int(input())


def mult(n):
    a = 0
    b = 0
    n = abs(n)
    while n > 0:
        if (n%10)%2 == 0:
            a += n%10
        else:
            b += n%10
        n = int(n/10)
    return a*b


print(mult(n))
