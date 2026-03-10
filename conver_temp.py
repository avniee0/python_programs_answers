choice=input("Enter your choice(F to c)/ (C to F):")
if choice=="F to C":
    F= float(input("Enter temp in fahrenheit:"))
    C=(5/9)*(F-32)
    print("Temprature in celcius:",C)
elif choice=="C to F":
    C= float(input("Enter temp in Celcius:"))
    F= C*9/5+32
    print("Temprature in Fahrenhit:",F)
else:
    print("Invalid choice")