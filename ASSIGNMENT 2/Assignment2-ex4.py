#4.
#Write a program that repeatedly asks the user for a letter, and then prints all the names in this list that
#contain that letter
#Names=[“Maria”,”Hala”,”Ghady”,”Ehsan”,”Joe”,”Zoe”]
#Ex: letter=a, the program would output
#Maria
#Hala
#Ghady
#Ehsan

names = ["Maria", "Hala", "Ghady", "Ehsan", "Joe", "Zoe"]

while True:
    letter = input("Enter a letter (or type 'exit' to quit): ")

    if letter.lower() == 'exit':
        break  
    
    new_names = []
    
    for name in names:
      if letter.lower() in name.lower():
        new_names.append(name)
    
    if len(new_names)>0:
      print("Names containing the letter",letter +":")
      for name in new_names:
        print(name)
    else:
      print("No names contain the letter",letter ) 
   






