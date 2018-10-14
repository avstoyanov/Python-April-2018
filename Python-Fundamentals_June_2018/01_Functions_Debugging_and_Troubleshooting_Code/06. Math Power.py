n = float(input())
p = int(input())


def power(n, p):
    m = n
    for times in range(1, p):
        n = n*m
    return n


res = power(n, p)
print(f"{res}")
