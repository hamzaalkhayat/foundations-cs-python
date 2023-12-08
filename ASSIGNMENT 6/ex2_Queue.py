class Node:
  # constructor
  def __init__(self,value,next):
    self.value=value
    self.next=next


# a linked list is a list of nodes
class LinkedList:
  def __init__(self):
    self.head=None
    self.tail=None
    self.size=0 # the number of nodes in the LL
    
  def isEmpty(self):
    return self.size==0
    
  def addAtTail(self,value):#O(1)
    n=Node(value,None)
    if self.size==0: # LL is empty
      self.head=n
      self.tail=n
      self.size=1
    else:
      self.tail.next=n
      self.tail=n
      self.size+=1



  def deleteHead(self): #O(1)
    if self.size==0:#O(1)
      return None#O(1)
    elif self.size==1:#O(1)
      temp=self.head.value #O(1)
      self.head=None#O(1)
      self.tail=None#O(1)
      self.size=0#O(1)
      return temp#O(1)
    # we have more than one node
    else:
      temp=self.head.value #O(1)
      self.head=self.head.next#O(1)
      self.size-=1
      return temp#O(1)



class Queue:
  def __init__(self):
    self.items=LinkedList()
    
  def enqueue(self,value): #O(1)
       
      input_str = value
      for char in input_str:
        self.items.addAtTail(char.lower()) #O(1)

  def dequeue(self): #O(1)
    if self.items.isEmpty():
      return None
    return self.items.deleteHead()
  def is_balanced (self ):
     
      braces = 0       #{}
      Parentheses = 0  #()
      brackets = 0   #[]
      
      while not self.items.isEmpty():
          x = self.dequeue()
          if x == '{' and braces >=0 :
              braces = braces + 1
          elif x == '}'  :
              braces = braces - 1
          elif x == '(' and Parentheses >=0 :
              Parentheses = Parentheses + 1
          elif x == ')' :
              Parentheses = Parentheses - 1
          elif x == '[' and brackets>=0 :
              brackets = brackets + 1
          elif x == ']' :
              brackets = brackets - 1
          else:
              braces = braces
              Parentheses = Parentheses
              brackets = brackets
              
      if  braces == 0 and Parentheses == 0 and brackets == 0 :
          print ("Output : True")
      else :
          print ("Output : False") 
         
          
q=Queue()

input_str = "(1+2)-3*[41+6]"  
print("Input : " + input_str)
q.enqueue(input_str)   
q.is_balanced()

input_str = "(1+2)-3*[41+6}" 
print("Input : " + input_str) 
q.enqueue(input_str)   
q.is_balanced()

input_str = "(1+2)-3*[41+6" 
print("Input : " + input_str) 
q.enqueue(input_str)   
q.is_balanced()

input_str = "(1+2)-3*]41+6[" 
print("Input : " + input_str) 
q.enqueue(input_str)   
q.is_balanced()

input_str = "(1+[2-3]*4{41+6})" 
print("Input : " + input_str)
q.enqueue(input_str)   
q.is_balanced()
              

      