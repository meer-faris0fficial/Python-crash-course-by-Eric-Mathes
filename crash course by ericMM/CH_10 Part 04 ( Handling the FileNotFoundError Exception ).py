# Handling the FileNotFoundError Exception

filename = 'alice.txt'
try:
    with open(filename, encoding='utf-8') as f:
    # encoding is the argument is needed when your system’s default encoding doesn’t match the encoding of
    #  the file that’s being read. 
        contents = f.read()
except FileNotFoundError:
    print(f"the file {filename} does not found.")
else:
   # Count the approximate number of words in the file.
     words = contents.split()
     num_words = len(words)
     print(f"The file {filename} has about {num_words} words.")    
    
    
#  Analyzing Text this will separate the each word of the string from the space and place it into the list
title = "Alice in the wonderland"
print(title.split())



