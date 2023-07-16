import math
a = int(input("enter a"))
b = int(input("enter b"))
c = int(input("enter c"))
d = (b**2) - (4*a*c)
root1=(-b+math.sqrt(d))/2*a
root2=(-b-math.sqrt(d))/2*a
if d==0:
    print("error")
else:
    print("root1 or root2")