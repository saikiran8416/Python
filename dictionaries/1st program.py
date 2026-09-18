"""Write code to:

Print the student's name
Print the score
Change the age to 26
Add "city": "Bangalore"
Delete course"""
student = {
    "name": "Rahul",
    "age": 25,
    "course": "Python",
    "score": 85
}

student.pop("course")
student["age"]=26
student["city"]="Bangalore"
print(f"student name: {student["name"]}")
print(f"score: {student["score"]}")
print(f"age: {student["age"]}")
print(f"city: {student["city"]}")
