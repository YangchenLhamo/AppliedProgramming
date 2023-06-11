def simple_interest(Principle, Rate, Time):
    simpleInterest=(Principle*Rate*Time)/100
    return simpleInterest

p=int(input("Enter the principle: "))
r=int(input('enter the rate:'))
t=int(input("enter the time: "))
print(simple_interest(p,r,t))