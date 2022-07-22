# A common punishment for school children is to write out a sentence multiple times.
# Write a Python stand-alone program that will write the
# following sentence one hundred times: "I will never spam my friends again."

def punishment(): #name of function
    
    print("I will never spam my friends again.") #output when fucntion is called
    
    
def littlenote(): # extra function that I added 
    print ("I will never spam my friends again.....this month") #output for this function
    

def main(): #main program  
    for i in range (100): # loop used to repeat punishment function 100 times
        
        punishment()
    
    for i in range(1): # loop used to print little note function; a little Bart simpson humor.
        
        littlenote()
    
main() #call main function so program can begin