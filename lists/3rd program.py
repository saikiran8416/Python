#Find the largest and smallest number without using max() or min()

numbers = [45, 12, 78, 34, 89, 23, 56]
max1=min1=numbers[0]
for i in numbers:
    if min1>i:
        min1=i
    if max1<i:
        max1=i
print(f"max: {max1}")
print(f"min: {min1}")
