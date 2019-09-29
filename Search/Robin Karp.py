'''Robin Karp Algorithm (With no hashing)'''
key="foss"
String="amfossamfossweloveamfoss"
for i in range(len(String)-len(key)):
    if(String[i]==key[0]): #instead of hashing we are checking the first character
        flag=True
        index=0
        while(flag and index<len(key)):
            if(String[i+index]!=key[index]):
                flag=False
            index+=1
        if(flag):
            print("String is found at index",i)
        
