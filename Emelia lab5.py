import random

# ==========================================
# Task 1: Print each character in user input
# ==========================================
x = input("Enter something: ")
for char in x:
    print(char)

# ==========================================
# Task 2: Numbers divisible by 5 (1-20)
# ==========================================
for num in range(1, 21):
    if num % 5 == 0:
        print(num)

# ==========================================
# Task 3: Decrement loop stopping at 4
# ==========================================
num = 10
while num > 0:
    if num == 4:
        break
    print(num)
    num -= 1

# ==========================================
# Task 4: Enumerate list items & calculate square
# ==========================================
numbers = [2, 5, 8, 11]
for index, val in enumerate(numbers):
    print(f"index {index}: Number = {val}, Square = {val**2}")

# ==========================================
# Task 5: Print students with grade > 80
# ==========================================
students_dict = {
    "Emelia": 89,
    "Mario": 78,
    "Jacob": 88,
    "Emiliy": 67
}
for name, grade in students_dict.items():
    if grade > 80:
        print(name)

# ==========================================
# Task 6: List comprehension for squares not divisible by 3
# ==========================================
num_square = [x**2 for x in range(1, 21) if (x**2) % 3 != 0]
print(num_square)

# ==========================================
# Task 7: Zip two lists and print pairs
# ==========================================
nums = [1, 2, 3]
alpha = ["a", "b", "c"]
for n, char in zip(nums, alpha):
    print(f"Pair: {char}-{n}")

# ==========================================
# Task 8: Random list, min, and max
# ==========================================
random_list = [random.randint(1, 50) for x in range(5)]
print("list", random_list)
print("Min", min(random_list))
print("Max", max(random_list))

# ==========================================
# Task 9: Collect names containing letter 'a'
# ==========================================
names_a = []
while True:
    name = input("Enter a name (or 'stop' to finish): ")
    if name.lower() == "stop":
        break
    if "a" in name.lower():
        names_a.append(name)
print("Names: ", names_a)

# ==========================================
# Task 10: Find highest grade using zip & enumerate
# ==========================================
names = ["Judy", "Michael", "Tiea", "Helana", "Kareen"]
grades = [79, 90, 67, 87, 94]

students = list(zip(names, grades))
random.shuffle(students)

highest_grade = -1
top_student_name = ""

for index, (name, grade) in enumerate(students):
    print(f"Index {index}: {name} scored {grade}")
    if grade > highest_grade:
        highest_grade = grade
        top_student_name = name

print(f"Highest grade: {top_student_name} scored {highest_grade}")
