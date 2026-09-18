# Find the student with the highest marks.
marks = {
    "Rahul": 78,
    "Priya": 92,
    "Arun": 85,
    "Sneha": 88
}
highest_marks=0
for i in marks:
    if highest_marks<marks[i]:
        highest_marks=marks[i]

print(f"highest marks: {highest_marks}")

