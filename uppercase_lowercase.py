string=input("Enter a string:")
count=0
for i in string:
    count+=1
if count>5:
    print(string.upper())
else:
    print(string.lower())