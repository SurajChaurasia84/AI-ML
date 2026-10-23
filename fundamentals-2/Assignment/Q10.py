secret_num = 84
num = int(input("Enter a number: "))

if num < secret_num:
    print("Too low!")
elif num > secret_num:
    print("Too high!")
else:
    print("You guessed it!")