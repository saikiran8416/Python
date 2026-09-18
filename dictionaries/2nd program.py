"""write a program to Ask the user for a key and check if the key exists in the program or not"""
employee = {
    "name": "Sai",
    "role": "QA Engineer",
    "experience": 4,
    "location": "Bangalore"
}

key=input("enter the key: ")
if key in employee:
    print("keys exists")
else:
    print("key does not exist")