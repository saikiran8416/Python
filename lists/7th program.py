#Separate even and odd numbers from a list
numbers = [12, 7, 8, 15, 22, 31, 40, 9]
even=[]
odd=[]
for i in numbers:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(f"even list: {even}")
print(f"odd list: {odd}")
