n = int(input())
l = int(input())
for one in range(1, n+1):
    print(one)
    for two in range(1, n+1):
        print(two)
        for three in range(1, l+1):
            print(chr(three + 96), end="")
            for four in range(1, l+1):
                print(chr(four + 96), end="")
                for five in range(max(one, two), n+1):
                    print(five)
