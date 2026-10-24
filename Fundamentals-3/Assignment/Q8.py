# Check if Two Lists Share No Common Elements (Using Sets)

list1 = [1, 2, 3, 5]
list2 = [5, 6, 7, 8]

# isdisjoint returns True if sets have no common elements
if set(list1).isdisjoint(set(list2)):
    print("The lists share NO common elements.")
else:
    print("The lists share common elements.")