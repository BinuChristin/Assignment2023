#Write a Python program to check the validity of a password input by the user. 
# #The password should satisfy the following conditions:

    #a. It should have at least 1 letter [a to z]
    #b. It should have at least 1 number [0 to 9]
    #c. It should have at least 1 capital letter [A to Z]
    #d. It should have at least one special character [$, #, @]
    #e. Minimum length = 6 characters
    #f. Maximum length = 12 characters


import re
password = str(input("enter password"))

regular_expression = "\w+\d+ +[A-Z]+[$#@]"

if len(password) >=6 or len(password)<=6:
    print("enter stronger password")
if re.search(password, regular_expression)==0:
    print("the password satifies the condition")
else:
    print("enter stronger password")