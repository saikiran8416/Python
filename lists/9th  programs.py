#Write a program to find the duplicate test ids
test_cases = [
    "TC001", "TC002", "TC003",
    "TC002", "TC004", "TC001",
    "TC005", "TC003"
]

dict1={}
dict2={}
for i in test_cases:
    if i in dict1:
        dict1[i]+=1
        if i in dict2:
            dict2[i]=dict1[i]
        else:
            dict2[i]=dict1[i]
    else:
        dict1[i]=1
duplicate_id_list=[]

for i in dict2:
    if dict2[i]>=2:
        duplicate_id_list.append(i)
print(duplicate_id_list)

"""output:
["TC002", "TC001", "TC003"]"""