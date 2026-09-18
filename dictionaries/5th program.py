#Find the values that occur more than once.
data = {
    "a": 10,
    "b": 20,
    "c": 10,
    "d": 30,
    "e": 20,
    "f": 40
}
ls1=[]
repeations=[]
for i in data:
    if data[i] in ls1:
        repeations.append(data[i])
    elif data[i] not in ls1:
        ls1.append(data[i])
    

print(repeations)