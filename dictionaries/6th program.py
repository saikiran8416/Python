#Write a program to swap key and values with one another in an dictionary
def swap_key_values(**kwargs):
    dict1={}
    for k,v in kwargs.items():
            dict1.setdefault(v,k)
    return dict1

data = {
    "fname": "Saikiran",
    "role": "QA",
    "city": "Bangalore",
    "nickname": "saikiran"
}

print(swap_key_values(**data))