#Create a new list containing only unique values:
numbers = [10, 20, 10, 30, 20, 40, 10, 50]


#using logic
ls1=[]
dict1={}
for i in numbers:
    if i in dict1:
        dict1[i]+=1
    else:
        dict1[i]=1
for i in dict1:
    if dict1[i]<=1:
        ls1.append(i)
print(dict1)
print(ls1)

#using type conversion
set1=set(numbers)
numbers=list(set1)
print(numbers)
