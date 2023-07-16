#Write a program that accepts a sentence and calculate the number of letters and digits. 
#Suppose the following input is supplied to the program: hello world! 123
#Then, the output should be:
#LETTERS 10
#DIGITS 3
 
import re

a = input("enter a string")

alpha_count = 0
number_count = 0

if a.isalpha():
    alpha_count+=1
    print("The number of words is", alpha_count)
elif a.isdigit():
    number_count+=1
    print("The number of digits are", number_count)