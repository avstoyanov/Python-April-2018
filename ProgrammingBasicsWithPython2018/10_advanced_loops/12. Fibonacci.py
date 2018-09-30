n = int(input()) +1
#uses phi to calculate or the Nth number of the fibonacci sieries
print(int((pow((1+pow(5, 0.5))/2, n) - pow(((1 - pow(5, 0.5))/2), n))/pow(5, 0.5)))
