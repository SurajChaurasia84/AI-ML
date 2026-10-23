# Write a function that takes two integers a and b and prints all even numbers between them (inclusive).

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

for i in range(num1,num2+1):
    if i%2==0:
        print(i)