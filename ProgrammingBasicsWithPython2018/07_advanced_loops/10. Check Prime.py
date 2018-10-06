n = int(input())
#placement value is hi
ans = "hi"
div = 2
if n == 2 or n == 3:
    ans = "Prime"
elif n <= 1:
    ans = "Not Prime"
else:
    while div <= pow(n, 0.5):
        if n % div == 0:
            ans = "Not Prime"
            break
        else:
            ans = "Prime"
            div += 1
print(ans)