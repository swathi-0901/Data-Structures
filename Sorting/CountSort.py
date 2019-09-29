'''Count Sort'''
import random

def CountSort(l):
    #Assuming the max value in the list will be less than or equal to 100
    #Initialising the array with zeroes 
    count_array=[0]*101
    for i in range(len(l)):
        count_array[l[i]]+=1
    index=0
    for i in range(len(count_array)): #Traversing across all the numbers
            while(count_array[i]>0):  #If its count is greater than Zero tehn inserting into Original Array
                l[index]=i
                count_array[i]-=1     #decreasing its count
                index+=1
    
                

def random_list(size,max_value):    #Generating a random list of specific size and Max value
    l=[]
    for i in range(size):
        l.append(random.randrange(0,max_value+1))
    return l

arr=random_list(20,100)
CountSort(arr)
print(*arr)

