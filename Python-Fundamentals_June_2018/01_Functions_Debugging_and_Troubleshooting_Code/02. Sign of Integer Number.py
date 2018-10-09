n = int(input())
def sign(n):
    if n == 0:
        return "zero"
    elif n < 0:
        return "negative"
    else:
        return "positive"
print(f"The number {n} is {sign(n)}.")
