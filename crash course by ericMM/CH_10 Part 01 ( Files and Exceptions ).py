# files and exceptions

# open a text file using open() we can also close the by using the call close()but it causes many errors
# and it is hard to know when should we close the file so it is preferable to use only open() and trust
# the python to file when the execution is done

# the digit.read() command add an empty string at the end of the executed file data which is displayed 
# as an empty line at the end of the output we can remove it by using the strip() command  
with open('pi_digits.txt') as digits:  # here file name must be in the commas and end of the line colon is must
    contents = digits.read()
print(contents) # output with an empty line at the end
print(contents.rstrip()) # output without an empty line at the end

#  File Paths
#  sometime the text from which we want to import data is in the another folder for which instead of using
#  file name we uses the file path that include the folder name as given below
#  first give the folder name then / then file name 
#  with open('text_files/filename.txt') as file_object: 

#  windows system only uses the backslash / in the file path but we can also uses the forward slash in
#  python  You can also tell Python exactly where the file is on your computer regardless of where
#  the program that’s being executed is stored. This is called an absolute file path

#  file_path = '/home/ehmatthes/other_files/text_files/filename.txt'
#  with open(file_path) as file_object:

#  using blackslashes in the file path can sometimes give an error as it is use in the escape charachters
#  like ( \t,\n,\'') so if we want to use a black slash we uses double black slash \\ 
#  as given "C:\\path\\to\\file.txt".

# reading line by line
filename = 'pi_digits.txt'
with open(filename) as file_objects:
    for file_object in file_objects:  # it will check the file data line by line
        print(file_object.rstrip())

#  Making a List of Lines from a File
with open(filename) as file_object:
    lines = file_object.readlines() # read every line in the program
    
for line in lines:
    print(line.rstrip())
# Working with a File’s Contents

pi_string = ''
for line in lines:
    pi_string += line.strip()  # python handle every element in the file as a string if we want to convert it to another type we must give the variable a type like int() float()

birthday = input("Entre your birthday in the format of the mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in a first 1000 values of the pi")
else:
    print("you birthday does not appear in the first 1000 values of the pi")


print(f"{pi_string[:20]}")  # print only first 20 element of the string in the file
print(len(pi_string)) # count every element of the file






