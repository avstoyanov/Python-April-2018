type = input()
fval = input()
sval = input()


def compare(val1, val2):
    if val1 > val2:
        return val1
    elif val1 < val2:
        return val2


res = compare(fval, sval)
print(res)
