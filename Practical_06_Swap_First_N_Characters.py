# Practical 6: Swap the first n characters of two strings
first = input("Enter the first string: ")
second = input("Enter the second string: ")
n = int(input("Enter n: "))

if n < 0 or n > len(first) or n > len(second):
    print("Invalid n. It must not exceed the length of either string.")
else:
    swapped_first = second[:n] + first[n:]
    swapped_second = first[:n] + second[n:]
    print("First string after swapping:", swapped_first)
    print("Second string after swapping:", swapped_second)
