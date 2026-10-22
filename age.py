try:
    age=int(input("enter a number"))
    if age<18:
        raise ValueError
    else:
        print("elegibale to vote")
except:
    print("not elegibale to vote")

