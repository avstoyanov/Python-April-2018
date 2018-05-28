num = int(input())
digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety", "one hundred"]
if 0 <= num < 20:
    print(digits[num])
elif 20 <= num <= 100:
    if digits[num % 10] == "zero":
        print(tens[num // 10 - 2])
    else:
        print(tens[num // 10 - 2] + " " + digits[num % 10])
else:
    print("invalid number")