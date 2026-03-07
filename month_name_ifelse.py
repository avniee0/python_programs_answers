month=input("Enter month name:")
if month=="january" or month=="march" or month=="may" or month=="july" or month=="august" or month=="october" or month=="december":
    print("31 days")
elif month=="april" or month=="june" or month=="september" or month=="november":
    print("30 days")
elif month=="february":
    print("28/29 days")
else:
    print("Enter valid month")
