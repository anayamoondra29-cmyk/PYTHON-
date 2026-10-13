def cube(x):
    print(x* x* x)
cube(5)
num=int(input("enter a number"))

def by_three(number):
    if number %3 ==0:
        return cube(number)
    else:
        return False
    
print(by_three(9))
print(by_three(4))


