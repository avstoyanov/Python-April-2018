bitcoin = float(input())
yuans = float(input())
fee = float(input())
bitlev = bitcoin * 1168
yollars = yuans * 0.15
yolevs = yollars * 1.76
euros = (bitlev + yolevs)/1.95
real_fee = (100-fee)/100
print("%.2f" % (euros * real_fee))
