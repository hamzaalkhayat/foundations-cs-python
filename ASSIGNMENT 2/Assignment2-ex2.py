# 2. Write a program that asks the user for a number n and outputs the below pattern. For
#example, if the user inputs 6 the following pattern is displayed:
#*
#**
#***
#****
#*****
#******


while True:
    n = input("Enter a number: ")

    if n.isdigit():
        number = int(n)
        break  # Exit the loop if a valid integer is provided
    else:
        print("Invalid input. Please enter a valid integer.")

for i in range(1, number + 1):
    
    output = ""
    for j in range(i):
        output += "*"
        
    print(output)