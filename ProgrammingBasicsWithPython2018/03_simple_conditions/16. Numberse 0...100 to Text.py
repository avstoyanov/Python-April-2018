num = int(input())
second = str(num % 10)
first = str(num // 10)
end = ""
if num == 0:
    end = "zero"
if num == 100:
    end = "one hundred"
elif second == "1":
    second = "one"
elif second == "2":
    second = "two"
elif second == "3":
    second = "three"
elif second == "4":
    second = "four"
elif second == "5":
    second = "five"
elif second == "6":
    second = "six"
elif second == "7":
    second = "seven"
elif second == "8":
    second = "eight"
elif second == "9":
    second = "nine"
if 0 < num < 10:
    end = second
elif 13 <= num < 20:
    end = second + "teen"
if 10 <= num < 20:
    if num == 10:
        end = "ten"
    elif num == 11:
        end = "eleven"
    elif num == 12:
        end = "twelve"
    elif num == 13:
        end = "thirteen"
    elif num == 15:
        end = "fifteen"
    elif num == 18:
        end = "eighteen"
elif 20 <= num < 100:
    if first == "2":
        first = "twenty"
    elif first == "3":
        first = "thirty"
    elif first == "4":
        first = "forty"
    elif first == "5":
        first = "fifty"
    elif first == "6":
        first = "sixty"
    elif first == "7":
        first = "seventy"
    elif first == "8":
        first = "eighty"
    elif first == "9":
        first = "ninety"
    if second != "0":
        end = first + " " + second
    else:
        end = first
if num < 0 or num > 100:
    end = "invalid number"
print(end)