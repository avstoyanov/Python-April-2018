numbers_list = list(map(int, input().split(" ")))
mult = int(input())
for num in numbers_list:
    print(num * mult, end=" ")
