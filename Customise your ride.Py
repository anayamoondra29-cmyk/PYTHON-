choice=(input("pick a car or a bike"))
if choice=="car":
    print("pick SUV or Small car")
    choice1=(input("enter your choice"))
    if choice1=="SUV":
     print("you have selected SUV")
    else:
        print("you have picked small car")
else:
   if choice=="bike":
      print("EV bike or Pertol bike")
      choice1=(input("enter your choice"))
      if choice1=="EV":
         print("you have picked EV")
      else:
         print("you have picked petrol bike")

