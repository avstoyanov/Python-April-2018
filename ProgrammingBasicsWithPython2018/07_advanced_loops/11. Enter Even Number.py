is_even = False
while is_even == False:
    n = float(input("Enter even number: "))
    if not n%1 == 0:
        print("Invalid number!")
    elif n%2 == 0:
        is_even = True
    else:
        print("The number is not even.")
print("Even number entered:", n)
