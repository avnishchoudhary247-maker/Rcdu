# Practical 4: Identify and analyse a character
digit_names = ["ZERO", "ONE", "TWO", "THREE", "FOUR",
               "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

character = input("Enter one character: ")

if len(character) != 1:
    print("Please enter exactly one character.")
elif character.isalpha():
    print("The character is a letter.")
    if character.isupper():
        print("It is an uppercase letter.")
    else:
        print("It is a lowercase letter.")
elif character.isdigit():
    print("The character is a numeric digit.")
    print("Digit in words:", digit_names[int(character)])
else:
    print("The character is a special character.")
