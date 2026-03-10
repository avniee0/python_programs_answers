list1=["ewr","wewe","123"]
result=True
for i in list1:
    for ch in i:
        if not ("a"<=ch<="z" or "A"<=ch<="Z"):
            result=False
print(result)
