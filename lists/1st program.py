"""Print the first element
Print the last element
Print the middle element
Print the list in reverse order"""

#program to print first, last, middle and reverse order of a list
numbers = [10, 20, 30, 40, 50]
print(f"first elelemt:{numbers[0]}")
print(f"last element:{numbers[-1]}")
print(f"middle element: {numbers[len(numbers)//2]}")
print(f"reverse order: {numbers[::-1]}")

