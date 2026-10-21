username = input("ENTER USERNAME : ")
password = input("ENTER PASSWORD : ")

if (username == "admin" and password == "pass"):
    print("LOGIN SUCCESSFUL!")
elif (username != "admin"):
    print("WRONG USERNAME")
else:
    print("WRONG PASSWORD")