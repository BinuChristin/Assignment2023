"""Write a program that accepts a sentence and calculate the number of letters
and deigits. spose the follwing input is supplied to the program: hello world! 123
then the output should be:
LETTERS 10
DIGITS 3"""


a=input("enter some words:")
x=y=0
for i in a:
    if i.isalpha():
        x=x+1
    elif i.isdigit():
        y=y+1
print("LETTERS ",x)
print("DIGITS ",y)




