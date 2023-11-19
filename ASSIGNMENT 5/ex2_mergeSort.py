# Sorting number in descending order
# We have wrote the function “merge sort”, change the code so that it sorts the numbers in descending
# order.
# Example: input:[3,5,1,8,-10]
# Output: [8,5,3,1,-10]


#merege Soret
def mergeSort(list1,start,end): #O(n log n)
  
  if start==end: #I have a list of length 1
    return
  mid=(start+end)//2 
  mergeSort(list1,start,mid) # dividing the list further
  mergeSort(list1,mid+1,end)
  merge(list1,start,mid,end) 
  
def merge(list1,start,mid,end): # to merge the two sublists into a sorted one, O(n), 
                                #n being the length of the list
  new_list=[]
  index1=start 
  index2=mid+1   
  
  while index1<=mid and index2<=end: 
    if list1[index1] > list1[index2]:
      new_list.append(list1[index1])
      index1+=1
      
    else: 
      new_list.append(list1[index2])
      index2+=1
  while index1<=mid:
      new_list.append(list1[index1])
      index1+=1
      
  while index2<=end: 
      new_list.append(list1[index2])
      index2+=1
    
  list1[start:end+1]=new_list   
 
     
list1=[3,5,1,8,-10]
mergeSort(list1,0,len(list1)-1)
print(list1)      