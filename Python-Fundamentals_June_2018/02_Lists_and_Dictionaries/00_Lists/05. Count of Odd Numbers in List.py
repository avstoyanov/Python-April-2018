num_list = list(map(int, input().split(" ")))
number_of_odds = 0
for num in num_list:
    if num%2 != 0:
        number_of_odds += 1
print(number_of_odds)
