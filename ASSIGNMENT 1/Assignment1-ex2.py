a=int(input("Enter your A value: "))
b=int(input("Enter your B value: "))
c=int(input("Enter your C value: "))

if a>b and a>c and b>c:
 print("The maximum value is a")
 print()
 print("The minimum value is c")
elif a>b and a>c and b<c:
 print("The maximum value is a")
 print()
 print("The minimum value is b")
elif b>a and b>c and a<c:
 print("The maximum value is b")
 print()
 print("The minimum value is a")
elif b>a and b>c and c<a:
 print("The maximum value is b")
 print()
 print("The minimum value is c")
elif c>a and c>b and b<a:
 print("The maximum value is c")
 print()
 print("The minimum value is b")
else:
 print("The maximum value is c")
 print()
 print("The minimum value is a")

