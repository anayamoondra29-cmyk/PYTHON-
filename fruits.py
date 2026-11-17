fruit_dict = {'Apple': 5, 'Banana': 2, 'Mango': 5, 'Orange': 3, 'Grapes':4 }

print("The fruit dictionary : " + str(fruit_dict))
target_value = 5
count = 0
for fruit in fruit_dict:
    if fruit_dict[fruit] == target_value:
        count = count + 1
        
print(fruit_dict)