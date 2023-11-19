# We have wrote the functions “insertion sort” and “selection sort. Change the code in
# one of them so that the function would sort the strings in an alphabetical order 
# (instead of ASCII).
# Example: input [“aA”, ”b”, “BD”, ”Bc”,”D”]
# Ouput:[“aA”, ”b”, ”Bc”, ”BD”, ”D”]

# SORET USING SELECTION
def selectionSort(list1): #O(n^2)
  border=0
  while border <len(list1)-1: #O(n), n being the length of the list
    minIndex=border 
    for i in range(border+1, len(list1)): # to find the index of the minimum element, O(n)
      if list1[i].lower()<list1[minIndex].lower(): #O(1), is the line that specifies the order
        minIndex=i                                 #Add .lower() to ensure case-insensitive alphabetical order.
                                   
    temp=list1[border] #O(1)
    list1[border]=list1[minIndex]
    list1[minIndex]=temp


    border=border+1
   
 
  
list1 = ["aA", "b","BD","Bc","D"]
selectionSort(list1)

print(list1)