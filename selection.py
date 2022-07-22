def selectionSort(sortlist):

   for s in range(len(sortlist)):

      # Find the minimum element in remaining
       minPosition = s

       for l in range(s+1, len(sortlist)):
           if sortlist[minPosition] > sortlist[l]:
               minPosition = l
                
       # Swap the found minimum element with minPosition       
       temp = sortlist[s]
       sortlist[s] = sortlist[minPosition]
       sortlist[minPosition] = temp

   return sortlist


sortlist = [1,2,3,4,5,6,7,8,9,10]
selectionSort(sortlist)
print(sortlist)



#Consider the first element to be sorted and the rest to be unsorted
#Assume the first element to be the smallest element.
#Check if the first element is smaller than each of the other elements:
#If yes, do nothing
#If no, choose the other smaller element as minimum and repeat step 3
#After completion of one iteration through the list, swap the smallest element with the first element of the list.
#Now consider the second element in the list to be the smallest and so on till all the elements in the list are covered.
#NOTE: Once an element is added to the sorted portion of the list, it must never be touched and or compared.

