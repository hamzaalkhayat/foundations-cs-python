
#1. Create a program that prompts the user for a number and returns the number of digits the
#    number contains.
#     EX: if the number is 3725, the program displays “3725 has 4 digits”.



user_input =input("Enter a number: ")
number_str = user_input.lstrip('-').replace('.', '')

while not(number_str.isdigit()):
    user_input =input("Invalid input. Please enter a valid number: ")
    number_str = user_input.lstrip('-').replace('.', '')
    
number_str1 = str(number_str)
digit_count = len(number_str1)

print(f"The number {user_input} contains {digit_count} digit{'s' if digit_count > 1 else ''}.")

