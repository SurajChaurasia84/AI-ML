# calculator

def calculator(a, b, operation):
    if operation == "+":
        print(a+b)
    elif operation == "-":
        print(a-b)
    elif operation == "*":
        print(a*b)
    elif operation == "/":
        print(a/b)
    else:
        print("Wrong Operation")

calculator(12,4,"/")