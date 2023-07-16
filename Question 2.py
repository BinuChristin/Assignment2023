"""write a program that reads in a string on the command line and returns a table of
 the frequency of occurrence of each word .ignore the case.a sample run of the
 program would look this enter some letters>>>the cat in the hat
 the - 2
 cat - 1
 in - 1 
 hat - 1"""""


txt = "the cat in the hat the cat in the hat"
x=txt.count("the")
y=txt.count("cat")
z=txt.count("in")
q=txt.count("hat")
print("the -",x)
print("cat -",y)
print("in -",z)
print("hat -",q)

