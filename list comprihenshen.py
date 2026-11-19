numbers=[1,2,3,4,5,6,7,8]
double=[]

for number in numbers:
    double.append(number*2)

print(double)
double=[numbers*2 for number in numbers]