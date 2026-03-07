string=input("Enter string:")
letter=input("Enter a letter:")

count=0
for i in string:
    if i==letter:
        count+=1
print("Frequency:",count)