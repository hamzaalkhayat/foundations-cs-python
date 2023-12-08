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
  def deleteTail(self): #O(n), n being the size of the LL
   if self.size <=1: # size == 0 or size ==1 
     return self.deleteHead()

   # size>=2
   current=self.head
   temp=self.tail.value
   # while current.next!=self.tail: #O(n)
   while current.next.next!=None:
     current=current.next

   current.next=None
   self.tail=current
   self.size-=1
   return temp
  def printLL(self):
    if self.size==0:
      print("my LL is empty")
    current=self.head
    while current!= None:
      print(current.value,"->",end=" ")
      current=current.next
    print()
    
  def deleteAtLocation(self, position):  
     
      position = position
      if self.size==0 or position < 0:#O(1)
          return None
   
     
      if position == 0:
         return self.deleteHead()
      elif position >0 and position < self.size - 1:
         current = self.head
         previous = None
         current_position = 0

         while current_position < position:
           previous = current
           current = current.next
           current_position += 1

         temp = current.value
         previous.next = current.next
         self.size -= 1
      elif position == self.size - 1:
          return self.deleteTail()

      
         
      return temp        
linked_list = LinkedList()
linked_list.addAtTail(12)
linked_list.addAtTail(56)
linked_list.addAtTail(76)
linked_list.addAtTail(11)
linked_list.addAtTail(0)

print("Original Linked List:")
linked_list.printLL()         
 
# linked_list.deleteAtLocation(4)
# print("\nLinked List after deleting at location :")
# linked_list.printLL()
   
linked_list.deleteAtLocation(3)
print("\nLinked List after deleting at location :")
linked_list.printLL()
     
linked_list.deleteAtLocation(0)
print("\nLinked List after deleting at location :")
linked_list.printLL()