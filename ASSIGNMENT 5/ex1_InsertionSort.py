# We have wrote the functions “insertion sort” and “selection sort. Change the code in
# one of them so that the function would sort the strings in an alphabetical order 
# (instead of ASCII).
# Example: input [“aA”, ”b”, “BD”, ”Bc”,”D”]
# Ouput:[“aA”, ”b”, ”Bc”, ”BD”, ”D”]

# SORET USING INSERTION
def insertionSort(list1): #O(n^2)
  border=1
  while border<len(list1): #O(n), n being the length of the list
    current=border # the index of the element we are currently dealing with
    while current>0 and list1[current].lower()<list1[current-1].lower(): #O(n)
                                   #Add .lower() to ensure case-insensitive alphabetical order.      
      #swap the out of order elements
       temp=list1[current]
       list1[current]=list1[current-1]
       list1[current-1]=temp
      
       current-=1
    border+=1


list1 = ["aA", "b","BD","Bc","D"]
insertionSort(list1)

print(list1)