# list students enrolled in Science

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

for name,course in info:
    if(course == "Science"):
        print(name)