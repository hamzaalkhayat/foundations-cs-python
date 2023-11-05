#3. Write a program that takes two integers from the user and outputs the range of values from this list
#list1=[54,76,2,4,98,100]. Make sure the values of the integers are valid. In case they are not, ask again.
#Ex: int1=20, int2=80. The program would print:
#54
#76


list1 = [54, 76, 2, 4, 98, 100]

x=min(list1)
y=max(list1)

int1 = int(input("Enter the first integer number : "))
int2 = int(input("Enter the Second integer number : "))

while int1<x or int1>y:
    int1 = int(input("Enter a valid integer 1 number : "))
while int2<x or int2>y:
    int2 = int(input("Enter a valid integer 2 number : "))

        
if int1 <= int2:
 for value in list1:
  if int1 <= value <= int2:
   print(value)
else:
 for value in list1:
  if int2 <= value <= int1:
   print(value)
