def bubbleSort(sortlist):
    
    for num in range(len(sortlist)-1,0,-1): #Setting the range for comparison (first round: n, second round: n-1  and so on)
        
        for s in range(num): ##Comparing within set range
            
            if sortlist[s]>sortlist[s+1]: #Comparing element with its right side neighbor
                
                temp = sortlist[s]
                 
                alist[s] = alist[s+1] #swapping
                
                alist[s+1] = temp

sortlist = [1,2,3,4,5,6,7,8,9,10]

bubbleSort(sortlist)

print(sortlist)



#For the first iteration, compare all the elements (n). For the subsequent runs, compare (n-1) (n-2) and so on.
#Compare each element with its right side neighbour.
#Swap the smallest element to the left.
#Keep repeating steps 1-3 until the whole list is covered.

