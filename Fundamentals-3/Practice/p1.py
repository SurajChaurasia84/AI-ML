# list all unique courses

info = [
    ("Alice","Math"),
    ("Bob","Science"),
    ("Biky","Science"),
    ("Amit","Math"),
    ("Bobby","Science"),
    ("Raj","Math"),
    ("Suraj","English"),
    ("Ali","English"),
]

courses_set = set()

for tup in info:
    courses_set.add(tup[1])
print(courses_set)
