grade=int(input("Enter the total grade: "))
if grade>100:
    print("The grade is error ")
elif grade>89 and grade<=100:
    print("A")
elif grade>79:
    print("B")
elif grade>69:
    print("C")
elif grade>59:
    print("D")
elif grade>=0 and grade<=59:
    print("F")
else:
    print("The grade is error ")

