def palind(r):
    e = len(r) -1
    s = 0
    while(s<e):
        if(r[s]!=r[e]):
            return False
        s+=1
        e-=1
    return True

r=(5,6,6,5)

if(palind(r)):
    print("the truple is a flip flop")
else:
    print("the truple is not a flip flop")