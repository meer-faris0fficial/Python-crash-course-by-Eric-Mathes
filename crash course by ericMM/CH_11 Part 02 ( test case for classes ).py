# test cases for the classes

# from survey import AnonymousSurvey
#  # Define a question, and make a survey.
# question = "What language did you first learn to speak?"
# my_survey = AnonymousSurvey(question)
# # Show the question, and store responses to the question.
# my_survey.show_question()
# print("Enter 'q' at any time to quit.\n")
# while True:
#     response = input("Language: ")
#     if response == 'q':
#         break
#     my_survey.store_response(response)
# # Show the survey results.
# print("\nThank you to everyone who participated in the survey!")
# my_survey.show_results()


# testing a class

import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    
    def test_store_single_response(self):
        question = "What language did you first learn to speak: "
        my_survey = AnonymousSurvey(question) # here anonynous(question) is use to call the class init function
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses) # survey.responses is a list name
        
    def test_three_responses(self):
        question = "What language did you first learn to speak: "
        my_survey = AnonymousSurvey(question)
        responses = ['English','Urdu','Hindi']
        for reponse in responses:
            my_survey.store_response(reponse) # store the above list in the method of the class 
        for reponse in responses:
            self.assertIn(reponse, my_survey.responses) # check the equality of reponse in the class
        
if __name__ == '__main__':
    unittest.main()
    
