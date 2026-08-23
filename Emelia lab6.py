# task1
def square(n):
    return n**2

def reverse_string(s):
    return s[::-1]

def add_numbers(a, b):
    return a + b

def is_even(n):
    return n % 2 == 0

def concat_strings(str1, str2):
    return str1 + str2

# task2
def square_list(numbers):
    result = []
    for num in numbers:
        result.append(num**2)
    return result

def countdown(n):
    while n > 0:
        print(n)
        n -= 1

def find_max(numbers):
    if not numbers:
        return None
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val

def sum_even_numbers(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
    return total

# task3a
def circle_area(r):
    pi = 3.14
    return pi * (r**2)

def celsius_to_fahrenheit(c):
    return (9/5) * c + 32

def compound_interest(p, r, n, t):
    return p * ((1 + (r / n)) ** (n * t))

# task3b
def activation_function(y):
    if y > 0:
        return 1
    else:
        return 0

def linear_function(m, x, c):
    return (m * x) + c

# task3c
def quadratic_formula(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "no real roots"
    root1 = (-b + discriminant**0.5) / (2 * a)
    root2 = (-b - discriminant**0.5) / (2 * a)
    return root1, root2
