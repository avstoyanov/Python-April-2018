money = float(input())
from_curr = input()
to_curr = input()
BG_val = 0
final_val = 0
# step 1 from 'any' ----> BG
if from_curr == "USD":
    BG_val = money*1.79549
if from_curr == "EUR":
    BG_val = money*1.95583
if from_curr == "GBP":
    BG_val = money*2.53405
if from_curr == "BGN":
    BG_val = money

# step 2 from BG ----> 'any'
if to_curr == "BGN":
    final_val = BG_val
if to_curr == "USD":
    final_val = BG_val/1.79549
if to_curr == "EUR":
    final_val = BG_val/1.95583
if to_curr == "GBP":
    final_val = BG_val/2.53405
print(round(final_val, 2), to_curr)
