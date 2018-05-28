workdays = int(input())
money_per_day = float(input())
dollar_conversion = float(input())
after_taxes = 0.75
bonus = workdays * money_per_day * 2.5
orig_yearly = money_per_day * workdays * 12
yearly_with_bonus = orig_yearly + bonus
final = yearly_with_bonus * 0.75
print("%.2f" % (final * dollar_conversion/365))