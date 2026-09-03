attendence=int(input("enter your attdennce %"))
if attendence>=75:
    print("you are elegible to take this test")
else:
    medicalcause=(input("do you have a medical cause Y=yes or N=No"))
    if medicalcause=="Y":
     print("You are eligible to take the test")
    else:
       print("you are not elgibal")


