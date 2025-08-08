import random

min_value = int(input("Enter a minimum value: "))
max_value = int(input("Enter a maximum value: "))

random_value = random.randint(min_value, max_value)
print(random_value)