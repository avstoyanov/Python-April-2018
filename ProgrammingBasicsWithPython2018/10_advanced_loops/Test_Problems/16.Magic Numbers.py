n = int(input())
for first in range(1, min(n+1, 10)):
    for second in range(1, min(n+1, 10)):
        for third in range(1, min(n+1, 10)):
            for fourth in range(1, min(n+1, 10)):
                for fifth in range(1, min(n+1, 10)):
                    for sixth in range(1, min(n+1, 10)):
                        if first*second*third*fourth*fifth*sixth == n:
                            print(str(first) + str(second) + str(third) + str(fourth) + str(fifth) + str(sixth), end=" ")
