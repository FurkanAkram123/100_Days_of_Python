import question_model
import data
import quiz_brain as qb

if __name__ == "__main__":
    #create an empty list to hold the question objects
    question_bank = []
    for text in data.question_data:
        
        #append the question_bank list with objects of the Question class
        question_bank.append(question_model.Question(text["question"], text["answer"]))
              
    quiz = qb.QuizBrain(question_bank)
    while quiz.still_has_questions():
        if quiz.next_question():

            #increment the score if the answer is correct
            quiz.score += 1

    #print the final score
    print(f"You've completed the quiz!", 
          f"Your final score was: {quiz.score}/{len(quiz.question_list)}", 
          sep="\n")

