# Print Elements Appearing More Than Once (Using Sets)

items = [1, 2, 3, 2, 4, 5, 6, 3, 7, 1]

seen = set()
duplicates = set()

for item in items:
    if item in seen:
        duplicates.add(item)
    else:
        seen.add(item)

print("Duplicates in the list:", list(duplicates))