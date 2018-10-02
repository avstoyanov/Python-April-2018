#untested version
n = int(input())
l = int(input())
for one in range(1, n+1):
    for two in range(1, n+1):
        for three in range(1, l+1):
            for four in range(1, l+1):
                for five in range(max(one, two)+1, n+1):
                    print(str(one) + str(two) + chr(three + 96) + chr(four + 96) + five, end=" ")
