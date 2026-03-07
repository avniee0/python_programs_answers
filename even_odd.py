start_no=int(input("Enter start no:"))
end_no=int(input("Enter end no:"))
even=0
odd=0
for i in range(start_no,end_no+1):
    if i%2==0:
        even+=1
    else:
        odd+=1
print("Even number:",even)
print("Odd number:",odd)