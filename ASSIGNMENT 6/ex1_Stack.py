class Stack:
  def __init__(self) :
    self.items=[]

  
  def isEmpty(self): #O(1)
    if len(self.items)==0:
      return True
    else:
      return False

  
  def push(self,value): #O(1)
    input_str = value
    for char in input_str:
        self.items.append(char.lower())
    

  def pop(self):#O(1)
    if self.isEmpty():
      return None
    return self.items.pop()


  def is_palindrome(self,x):
      
      input_str=x 
      return_str = ""
      
      while not self.isEmpty():
          return_str += self.pop()
      if input_str.lower() == return_str.lower():
         print("THE String is palindrome.")
      else:
         print("THE String is not palindrome.") 






s=Stack()

input_str = "Neveroddoreven"
print("Input : " + input_str)
s.push(input_str)
s.is_palindrome(input_str)


input_str = "mom"
print("Input : " + input_str)
s.push(input_str)
s.is_palindrome(input_str)


input_str = "khjsgfu" 
print("Input : " + input_str)
s.push(input_str)
s.is_palindrome(input_str)
