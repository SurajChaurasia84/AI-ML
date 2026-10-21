color = input("Enter Color: ")

match color:
    case "green":
        print("go")
    case "yellow":
        print("look")
    case "green":
        print("Stop")

    # deafult case
    case default:
        print("wrong color")