# Write a program to perform the following tasks:
#Ask a user to enter two lists: one list contains the name of the people and other list contains their marks.
#Map the two lists into a dictionary, and print the dictionary line by line.
#Print the dictionary, sorted by their names.
#Check if a key exists in the dictionary, then remove the key-value pair and confirm the changes in the dictionary.
#Ask the user for the name of a new student, add it to the dictionary and display the final dictionary.


# creating an empty list

names = []
marks = []
   
names = [item for item in input("Enter the names : ").split()] 
marks = [item for item in input("Enter the marks : ").split()]
  
print(names)
print(marks)

user_info = dict(zip(names, marks))
print(sorted(user_info))

if 'James' in user_info:
  print("Yes, 'James' is one of the keys in the this dictionary")
          
else: 
        print("The key does not exist in the dictionary.")
        
        
        