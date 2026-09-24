num=int(input("enter a number"))
count=0
temp=num
while temp > 0 :
    digit = temp % 10
    count=count+1
    temp//=10
print("number of digits",count)
