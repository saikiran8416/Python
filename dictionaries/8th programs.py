from collections import Counter
text = "aabbcdeeff"
dict1=Counter(text)
for i in dict1:
    if dict1[i]==1:
        print(i)
        break

#logic
text = "aabbcdeeff"
dict2={}
for i in text:
    if i in dict2:
        dict2[i]+=1
    else:
        dict2[i]=1
for i in dict2:
    if dict2[i]==1:
        print(i)
        break