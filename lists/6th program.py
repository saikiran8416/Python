#Find the second-largest unique number.
numbers = [10, 45, 23, 89, 67, 89, 34]
max1=numbers[0]
max2=0
for i in numbers:
    if max1<i:
        max1=i
for i in numbers:
    if max2<max1 and i>max2 and i<max1:
        max2=i
print(f"Second largest number: {max2}")
