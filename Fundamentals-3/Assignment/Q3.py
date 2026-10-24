# Input comma-separated integers from user
list1 = [int(x) for x in input("Enter first list numbers: ").replace(',', ' ').split()]
list2 = [int(x) for x in input("Enter second list numbers: ").replace(',', ' ').split()]

merged_list = list1 + list2
merged_list.sort()

print("Merged and sorted list:", merged_list)