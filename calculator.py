def add(x,y):
    print(x+y)

def sub(x,y):
    print(x-y)

def multlipication(x,y):
    print(x*y)

def division(x,y):
    print(x-y)

print("1.addition 2.substraction 3.multiplication 4.divison")
choice=int(input("enter your choice"))

number=int(input("enter a number"))

number2=int(input("enter a number"))

if choice==1:
    print(add(number,number2))

elif choice==2:
    print(sub(number,number2))

elif choice==3:
    print(multlipication(number,number2))

else:
    print(division(number,number2))
