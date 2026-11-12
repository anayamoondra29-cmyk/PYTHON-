frequancy={"tomato":2,"cucumber":4,"apple":9,"oranges":4}

print(frequancy)

value=int(input("which frequancy of fruits and vegtable do you want to check"))

res=0

for key in frequancy:
    if frequancy[key]==value:
        res=res+1

print(res)