# Design a program to continuously input a number n from user & print if it is positive or negative until the user enters “Quit”.

while True:
    n = input("Enter number: ")
    if (int(n)>0):
        print("Positive")
    elif(int(n)<0):
        print("Negative")
    