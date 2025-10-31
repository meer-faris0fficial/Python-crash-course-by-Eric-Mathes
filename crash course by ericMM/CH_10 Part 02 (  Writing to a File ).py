#  Writing to a File
#  We can open a file in the  read mode ('r'), write mode ('w'), append mode ('a'), or a mode that allows 
#  you to read and write to the file ('r+') these are place in the open funtion after the file name

file_name = 'programming.txt'
with open(file_name, 'w') as file_object: # it create a new file in the same folder and write down the following 
    file_object.write("I love programming.\n") # statement
    #  Writing Multiple Lines if the escape charachters are not added then it write on the same line 
    file_object.write("I love creating new games\n") # no new line added
# Appending to a File
with open(file_name, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")    
    
#  However, be careful opening a file in write mode ('w') because if the file does exist,Python will 
#  erase the contents of the file before returning the file object.

# Python can only write strings to a text file. If you want to store numerical data in a 
# text file, you’ll have to convert the data to string format first using the str() function.

