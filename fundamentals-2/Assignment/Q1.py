# Write a program that takes salary as input. Using conditional statements,calculate the final tax rate based on these rules:

# If salary < 30,000 → 5%
# If salary is 30,000–70,000 → 15%
# If salary > 70,000 → 25%


salary = int(input("Enter salary: "))

if salary < 30000:
    print("final tax rate =",salary*0.05)
elif (salary>= 30000 and salary <=70000):
    print("final tax rate =",salary*0.15)
elif (salary > 70000):
    print("final tax rate =",salary*0.25)