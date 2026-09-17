"""Change "banana" to "mango"
Add "grapes" at the end
Add "watermelon" at index 1
Remove "orange"""

fruits = ["apple", "banana", "orange"]
fruits[1]="mango"
fruits.append("grapes")
fruits.insert(1,"watermelon")
print(fruits)