def insertionSort(sortlist):
    
   for num in range(1,len(sortlist)): #element to be compared

     currentvalue = sortlist[num]
     
     position = num

     while position>0 and sortlist[position-1]>currentvalue:  #comparing the current element with the sorted portion and swapping
         sortlist[position]=sortlist[position-1]
         position = position-1

     sortlist[position]=currentvalue
     

sortlist = [1,2,3,4,5,6,7,8,9,10]
insertionSort(sortlist)
print(sortlist)




#Algorithm
#Consider the first element to be sorted and the rest to be unsorted
#Compare with the second element:
#If the second element< the first element, insert the element in the correct position of the sorted portion
#Else, leave it as it is
#Repeat 1 and 2 until all elements are sorted
#NOTE: As the number elements in the sorted portion increases, the new element from the unsorted portion must be compared with all the elements in the sorted list before insertion.

