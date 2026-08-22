#task1
def is_even(number):
    if number%2==0:
        return number

print(is_even(4))
print(is_even(5))

#task2
def countdown(start):
    while start>=0:
        print(start,end=" ")
        start--

print(countdown(5))

#task3
def classify_grade(grade):
    if grade>=80:
        return "Distincton"
    elif grade>=65:
        return" Merit"
    elif grade>=50:
        return "pass"
    else:
        return "fail"

#task4
def find_prime_numbers(limit):
    prime=[]
    for num in range(2, limit+1):
        is_prime=True
        for i in ranage(2, num):
            if num % i ==0:
                is_prime= False
                break
        if is prime:
            prime.append(num)

    return prime

print(find_prime_numbers(15))

#task5
import math

def calculate_stats_manually(temperature_data):
    if isinstance(temperature_data, dict):
        items = temperature_data.items()
    else:
        items = [(f"City {i+1}", temps) for i, temps in enumerate(temperature_data)]

    for city_name, temps in items:
        n = len(temps)
        max_temp = temps[0]
        min_temp = temps[0]
        total_sum = 0
        
        for t in temps:
            if t > max_temp:
                max_temp = t
            if t < min_temp:
                min_temp = t
            total_sum += t
            
        mean_val = total_sum / n
        variance_sum = sum((t - mean_val) ** 2 for t in temps)
        std_dev = math.sqrt(variance_sum / n)
        
        print(f"{city_name}: Max = {max_temp}, Min = {min_temp}, Std Dev = {std_dev:.2f}")

#task6
def check_consecutive_repeats(temperature_data):
    for idx, temps in enumerate(temperature_data, start=1):
        found_repeat = False
        
        for i in range(len(temps) - 1):
            if temps[i] == temps[i + 1]:
                print(f"City {idx}: Repeated value {temps[i]} found at positions {i} and {i + 1}")
                found_repeat = True
                break
                
        if not found_repeat:
            print(f"City {idx}: No consecutive repeated values")
