n1 = int(input())
n2 = int(input())
operator = input()
if n2 == 0:
    print("Cannot divide {} by zero".format(n1))
else:
    numType = ""
    operation = eval(str(n1) + operator + str(n2))
    if operator == "+" or operator == "-" or operator == "*":
        if operation % 2 == 0:
            numType = "even"
        else:
            numType = "odd"
        print(n1, operator, n2, "=", operation, "-", numType)
    elif operator == "/":
        print(n1, operator, n2, "=", "{0:.2f}".format(operation))
    else:
        print(n1, operator, n2, "=", operation)