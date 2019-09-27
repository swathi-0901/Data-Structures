'''Binary Search'''
import random
def BinarySearch(arr, start,end, key): 
    while start <= end: 
  
        mid = (start+end)//2; 
          
        # Check if key is present at mid 
        if arr[mid] == key: 
            return mid 
  
        # If key is greater, ignore left part of the array
        elif arr[mid] < key:
            start= mid + 1
  
        # If key is smaller, ignore right part of the array
        else: 
            end = mid - 1
    #If element not present
    return -1
def random_list(size,max_value):    #Generating a random list of specific size and Max value
    l=[]
    for i in range(size):
        l.append(random.randrange(0,max_value+1))
    return l
arr=random_list(20,100)
arr.sort()
print(*arr)
print(BinarySearch(arr,0,20,23),BinarySearch(arr,0,20,arr[0]))
