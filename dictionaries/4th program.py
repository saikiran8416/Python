#write a program to count the numbers of letter and their repeatation
text="automation"
counting={}
for i in text:
    if i in counting:
        counting[i]+=1
    else:
        counting[i]=1
print(counting) 

""" output:
{'a': 2, 'u': 1, 't': 2, 'o': 2, 'm': 1, 'i': 1, 'n': 1}
"""