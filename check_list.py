list1=["test@gmail.com","te@rere"]
valid=True

for i in list1:
    if "@" not in i or "." not in i:
        valid=False
if valid:
    print("Valid email list")
else:
    print("Invalid email list")