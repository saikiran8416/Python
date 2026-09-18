#create a single dictionary instance containing key and values of both the given dictionary

def combinedict(dict1,dict2):
    combineddict={}
    for k,v in dict1.items():
        combineddict.setdefault(k,v)
    for k,v in dict2.items():
        combineddict.setdefault(k,v)
    return combineddict

dict1 = {
    "name": "Sai",
    "age": 28,
    "city": "Bangalore"
}

dict2 = {
    "role": "QA Engineer",
    "experience": 4,
    "company": "BTL"
}

print(f"combine dictionary:\n {combinedict(dict1,dict2)}")