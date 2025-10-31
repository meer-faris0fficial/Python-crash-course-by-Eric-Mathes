# Testing your code
#  Unit Tests and Test Cases :
# unit test is a module from the python library provide tools for testing your coded


# from name_functions import get_formatted_name
# print("Entre 'q' to quit the program at any time.")

# while True:
#     first = input("\nPlease entre the first name: ")
#     if first == 'q':
#         break
#     second = input("Please entre the last name: ")
#     if second == 'q':
#         break
    
#     foramted_name = get_formatted_name(first, second)
#     print(f"\tNeatly formated name: {foramted_name}")

# a passing test 

import unittest
from name_functions import get_formatted_name

class Nametestcase(unittest.TestCase): # here class nametestcase iherit from unittest
    
    def test_first_last(self):  # here function name must be start with "test_" otherwise test case will ignore it
        foramted_name = get_formatted_name('tahir','hussain')
        self.assertEqual(foramted_name, 'Tahir Hussain')
        
    def test_first_last_middle_name(self):
        """Do names like 'Wolfgang Amadeus Mozart' work?"""
        formatted_name = get_formatted_name(
           'wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')
        
if __name__ == '__main__':
    unittest.main()
    


