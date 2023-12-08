class Stack:
  def __init__(self) :
    self.items=[]

  
  def isEmpty(self): #O(1)
    if len(self.items)==0:
      return True
    else:
      return False

  
  def push(self,value): #O(1)
      self.items.append(value)
      

  def pop(self):#O(1)
    if self.isEmpty():
      return None
    return self.items.pop()

  def decode_message(self,x):
      
      input_str = x
      decoded_message = ""
      for char in input_str:
          
         if char.isalpha() or char.isspace() :
            self.push(char) 
         elif char == '*' : 
            decoded_message += self.pop()
            
      while not self.isEmpty():
            decoded_message += self.pop()
           
      return decoded_message 

s=Stack()
   
message = "SIVLE ****** DAED TNSI ***"
decoded_message=s.decode_message(message)
print("Input : " + message)
print("Output : " + decoded_message)

