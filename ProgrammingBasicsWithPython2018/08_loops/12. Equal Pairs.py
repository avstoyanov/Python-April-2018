sets = int(input())
currsum = int(input()) + int(input())
maxdiff = 0
for num in range(1, sets):
    num1 = int(input())
    num2 = int(input())
    if abs(currsum - (num2+num1)) > maxdiff:
        maxdiff = abs(currsum - (num2+num1))
    currsum = num1 + num2
if maxdiff > 0:
    print("No, maxdiff=" + str(maxdiff))
else:
    print("Yes, value=" +














          

          str(currsum))