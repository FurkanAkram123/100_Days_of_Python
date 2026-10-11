import random

class QuizBrain:
    def __init__(self, list):
        self.question_number = 0
        self.selection_number = 0
        self.list_of_questions_asked = []
        self.score = 0
        self.question_list = list

    def next_question(self):

        #loop to generate a random number and check if it has been asked before
        while True:
            self.selection_number = random.randint(0, len(self.question_list) - 1)
            if self.selection_number not in self.list_of_questions_asked:
                break

        #add the new number to the list of questions asked and increment question number
        self.list_of_questions_asked.append(self.selection_number)
        self.question_number += 1
        
        #extract the question and answer from the question object list 
        current_question = self.question_list[self.selection_number].q
        answer = self.question_list[self.selection_number].a.lower()

        #Ask the question and put the answer in lowercase
        user_answer = input(f"Q#{self.question_number}: {current_question}").lower()
        
        #remove all spaces for the answer
        user_answer = user_answer.replace(" ", "")
        return user_answer == answer 
    
    def still_has_questions(self):
        #Evaluate if the question number is less than the length of the question list
        return self.question_number < len(self.question_list)

        