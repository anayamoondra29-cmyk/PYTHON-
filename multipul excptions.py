try:
    num1, num2 = eval(input("Enter two numbers, seprat by a comma"))
    result = num1 / num2
    print("result is" , result)
except ZeroDivisionError:
    print("Divsion by zero is error !!")

except SyntaxError:
    print("commas is missing. Enter a numbers seprated by comma like this 1, 2")
except:
    print("Wrong input")
else:
    print("no exeption")
finally:
    print("This will exucute no matter what")