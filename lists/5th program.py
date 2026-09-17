numbers = [1, 2, 3, 2, 4, 2, 5, 3, 1, 2]
occ_count={}
for i in numbers:
    if i in occ_count:
        occ_count[i]+=1
    else:
        occ_count[i]=1
for i in occ_count:
    print(f"{i}->{occ_count[i]}")


"""Output:
1->2
2->4
3->2
4->1
5->1
"""