# Practical 8: Cubes of even integers in an input list
items = input("Enter list elements separated by spaces: ").split()

numbers = []
for item in items:
    try:
        numbers.append(int(item))
    except ValueError:
        pass  # Ignore elements that are not integers.

# Method 1: Using a for loop
cubes_for_loop = []
for number in numbers:
    if number % 2 == 0:
        cubes_for_loop.append(number ** 3)

# Method 2: Using list comprehension
cubes_comprehension = [number ** 3 for number in numbers if number % 2 == 0]

print("Using for loop:", cubes_for_loop)
print("Using list comprehension:", cubes_comprehension)
