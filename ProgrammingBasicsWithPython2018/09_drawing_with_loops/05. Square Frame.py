length = int(input())
print("+ " + "- " * (length-2) + "+" )
for row in range(1, length - 1):
    print("| " + "- " * (length-2) + "|")
print("+ " + "- " * (length-2) + "+" )