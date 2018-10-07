name = input()
age = int(input())
town = input()
salary = float(input())
print("Name: "+name)
print("Age: "+age)
print("Town: "+town)
print(f"Salary: ${salary}:.2f")
if age< 18:
    age = "teen"
elif age<70:
    age = "adult"
else:
    age = "elder"
if salary < 500:
    salary = "low"
elif salary < 500:
    salary = "medium"
else:
    salary = "high"
print("Age range: "+age)
print("Salary Range: " + salary)