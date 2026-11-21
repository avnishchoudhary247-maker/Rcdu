# Practical 7: Find all starting indices of the second string in the first
def find_occurrences(first_string, second_string):
    if second_string == "":
        return -1

    indices = []
    start = 0
    while True:
        index = first_string.find(second_string, start)
        if index == -1:
            break
        indices.append(index)
        start = index + 1  # Also finds overlapping occurrences.

    return indices if indices else -1


first = input("Enter the first string: ")
second = input("Enter the second string: ")
print("Indices:", find_occurrences(first, second))
