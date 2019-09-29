'''Selection Sort'''
def swap(l,i,j):
    #swaping the ith element with jth element
    l[i],l[j]=l[j],l[i]
    
def SelectionSort(l):
    #I'th_MinElement
    n=len(l)
    for i in range(n-1):
        ith_min=l[i]
        index=i
        for j in range(i+1,n): #Finding the Ith min element in the I'th iteration
            if(l[j]<ith_min):
                index=j       #Storing the index of that min value
                ith_min=l[j]
        #After finding the min we have to swap it with the value in index "i"
        swap(l,index,i)

#Taking some random list
l=[9,99,9,1,2,2,9,1,2,3,4,5,2,2,8,6,6]
SelectionSort(l)
print(*l)
