number=input("Enter a number:")
even=0
odd=0
for i in number:
    if int(i)%2==0: #int(i) use for conver string into single digits
        even+=1
    else:
        odd+=1
print("Even nummber:",even)
print("Odd number:",odd)