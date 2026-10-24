# Given a list of integers compute the average of all numbers in the list.

numbers = [10, 20, 30, 40, 50]

if len(numbers) > 0:
    avg = sum(numbers) / len(numbers)
    print("Average:", avg)
else:
    print("List is empty.")