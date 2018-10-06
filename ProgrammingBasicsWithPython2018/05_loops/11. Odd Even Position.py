nums = int(input())
if nums == 0:
    print("OddSum=0, OddMin=No, OddMax=No, EvenSum=0, EvenMin=No, EvenMax=No")
elif nums == 1:
    first = input()
    print("OddSum={}, OddMin={}, OddMax={}, EvenSum=0, EvenMin=No, EvenMax=No".format(first, first, first))
else:
    nextodd = float(input())
    nexteven = float(input())
    oddmax = nextodd
    evenmax = nexteven
    oddmin = nextodd
    evenmin = nexteven
    sum1 = nextodd
    sum2 = nexteven
    for num in range(2, nums):
        curr = float(input())
        if not (num % 2 == 0):
            if curr > evenmax:
                evenmax = curr
            if curr < evenmin:
                evenmin = curr
            sum2 += curr
        else:
            if curr > oddmax:
                oddmax = curr
            if curr < oddmin:
                oddmin = curr
            sum1 += curr
    if oddmax%1 == 0:
        oddmax = int(oddmax)
    if oddmin%1 == 0:
        oddmin = int(oddmin)
    if evenmax%1 == 0:
        evenmax = int(evenmax)
    if evenmin%1 == 0:
        evenmin = int(evenmin)
    if sum2%1 == 0:
        sum2 = int(sum2)
    if sum1%1 == 0:
        sum1 = int(sum1)
    print("OddSum={}, OddMin={}, OddMax={}, EvenSum={}, EvenMin={}, EvenMax={}".format(sum1, oddmin, oddmax, sum2, evenmin, evenmax))

