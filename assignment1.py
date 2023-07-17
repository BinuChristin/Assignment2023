# 1
"""
import sys
import math

a = int(input("enter value for a"))
if a == 0:
    print("a cannot be zero")
    sys.exit()
b = int(input("enter value for b"))
c = int(input("enter value for c"))

w = math.sqrt((b * b) - (4 * a * c))
b1 = (-b + w) / (2 * a)
b2 = (-b - w) / (2 * a)

if w > 0:
    print("the roots are real and distinct")
    print("The roots are:", b1, b2)
elif w == 0:
    print("the roots are real and equal")
    print("The roots are:", b1, b2)
else:
    print("ERROR")
    print("roots are complex")
"""

# 2
"""
    
sentence = input("enter a string")
x = sentence.split(" ")
y = []
for i in x:
    if y.count(i) == 0:
       y.append(i)
       print(i.title(), "-", sentence.count(i))
"""

# 3
"""
import re
a = input("enter a string")
x = re.findall("[a-z]", a)
x1 = re.findall("[A-Z]", a)
l = len(x) + len(x1)
y = re.findall("\d", a)
d = len(y)
print("LETTERS:", l)
print("DIGITS:", d)
"""

# 4
"""
import re
import sys
a = input("enter a string")
x = re.split("", a)

if 6 < len(a) < 12:
    print("length is correct")
else:
    print("try again, length should be minimum 6 and maximum 12 characters")
    sys.exit()

b1 = re.findall("[a-z]", a)
b2 = re.findall("[A-Z]", a)
b3 = re.findall("\d", a)
b4 = re.findall("@#$", a)
a1 = len(b1)
a2 = len(b2)
a3 = len(b3)
a4 = len(b4)

if a1 == 0:
    print("It should have at least one small letter ,try again")
    sys.exit()
if a2 == 0:
    print("It should have at least one capital letter, try again")
    sys.exit()
if a3 == 0:
    print("It should have at least one digit, try again ")
    sys.exit()
if a4 == 0:
    print("It should have at least one special character, try again ")
    sys.exit()

if a1 > 0 and a2 > 0 and a3 > 0 and a4 > 0:
    print("password is valid")
else:
    print("password is invalid")
"""

# 5
"""
import re
a = input("enter the string")
b = input("enter the target word")
c = re.split(" ", a)
indexposition = []

i = 0
for l in c:
    if not b == l :
        i += 1
    else:
        indexposition.append(i)
        i += 1
if len(indexposition) == 0:
    print("FALSE")
else:
    print(indexposition)
"""











