list1=[3,9,5,7,]
list2=[5,3,2,2,4]
def add(x,y):
    return x+y
res = map(add, list1,list2)
print(list(res))