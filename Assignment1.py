'''

#Write a procedure that solves quadratic equations using the quadratic formula: It should
#take as arguments three numbers a, b, and c. It should print error messages if a is zero,
#or if the roots are complex. Otherwise it should print the two roots.
import math

a = int(input("Enter the 1st number: "))
b = int(input("Enter the 2nd number: "))
c = int(input("Enter the 3rd number: "))

if a == 0:
    print("Error: 'a' cannot be zero.")
else:
    discriminant = b**2 - 4*a*c

    if discriminant < 0:
        print("Error: Roots are complex.")
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)

        print("Root 1:", root1)
        print("Root 2:", root2)

#Write a program that accepts a sentence and calculate the number of letters and digits. Suppose the
#following input is supplied to the program: hello world! 123 Then, the output should be:
#LETTERS 10
#DIGITS 3
sentence = input("Enter a sentence: ")
letter_count = 0
digit_count = 0

for char in sentence:
    if char.isalpha():
        letter_count += 1
    elif char.isdigit():
        digit_count += 1


print("LETTERS", letter_count)
print("DIGITS", digit_count)


#Write a Python program to check the validity of a password input by the user. The password should
#satisfy the following conditions:
#a.	It should have at least 1 letter [a to z]
#b.	It should have at least 1 number [0 to 9]
#c.	It should have at least 1 capital letter [A to Z]
#d.	It should have at least one special character [$, #, @]
#e.	Minimum length = 6 characters
#f.	Maximum length = 12 characters

password = input("Enter a password: ")

valid = True

required_conditions = [any(char.isalpha() for char in password),
                       any(char.isdigit() for char in password),
                       any(char.isupper() for char in password),
                       any(char in ['$', '#', '@'] for char in password)]

if not all(required_conditions):
    valid = False

if valid:
    print("Valid password")
else:
    print("Invalid password")


#Write a Python program that takes a string of words separated by spaces, together with a ”target”
#word, and shows the position of the target word in the string of words.
#For example, if the string is: ‘we dont need no education we dont need no thought control no we dont’
#and the target word is ”dont”, then your program should return the list 1, 6, 13 because ”dont”
#appears at the 1st, 6th, and 13th position in the string. Your program should return False if the
#target word doesn’t appear in the string.

string_of_words = input("Enter a string of words: ")
target_word = input("Enter the target word: ")

words = string_of_words.split()
positions = []

for i in range(len(words)):
    if words[i] == target_word:
        positions.append(i + 1)

if positions:
    print(positions)
else:
    print(False)
'''