month=input("Enter month name:")
match month:
    case "january" | "march" | "may" | "july" | "august" | "october" | "decemmber":
        print("31 days")
    case "april" | "june" | "september" | "november":
        print("30 days")
    case "february":
        print("28/29 days")
    case _:
        print("Invalid month")