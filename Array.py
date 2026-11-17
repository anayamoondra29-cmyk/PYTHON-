import array as arr
array_num = arr.array('i' , [1,3,5,7,9,2,2,2,2,2])

print("Orignial array:  "+str(array_num))

print("Number of occurrsences of number 2 in the said array:  "+str(array_num.count(3)))

array_num.reverse()

print("reverse the order of items: ")

print(str(array_num))

