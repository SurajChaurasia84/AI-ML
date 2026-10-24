numbers_tuple = (12, 7, 9, 14, 22, 33, 40, 55)

even_list = []
odd_list = []

for num in numbers_tuple:
    if num % 2 == 0:
        even_list.append(num)
    else:
        odd_list.append(num)

even_tuple = tuple(even_list)
odd_tuple = tuple(odd_list)

print("Even numbers tuple:", even_tuple)
print("Odd numbers tuple:", odd_tuple)