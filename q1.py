#Write a procedure that solves quadratic equations using the quadratic formula: 
#It should take as arguments three numbers a, b, and c. It should print error messages if a is zero, or if the roots are complex. 
#Otherwise it should print the two roots.
#(-b±√(b²-4ac))/(2a) .


import math

a = int(input("enter a: "))
b = int(input("enter b: "))
c= int(input("enter c: "))

var1= (b**2) - (4*a*c)
x1 = int(-(b)+math.sqrt(var1)/(2*a))
x2 = int(-(b)-math.sqrt(var1)/(2*a))

if var1==0 or var1<0:
    print("error")
    
else: 
    print("The roots are", x1, "or", x2)

 

