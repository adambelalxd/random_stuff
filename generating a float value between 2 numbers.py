import random

min_value = float(input("Enter a minimum number: "))
max_value = float(input("Enter a maximum number: "))

random_float = random.uniform(min_value, max_value)
print(f"{random_float:.2f}")