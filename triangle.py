import math
a=int(input("Enter first side: "))
b=int(input("Enter second side: "))
c=int(input("Enter third side: "))
s=(a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print (area)