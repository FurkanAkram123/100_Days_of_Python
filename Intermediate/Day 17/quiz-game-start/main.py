import question_model
import data
import quiz_brain as qb
import random

if __name__ == "__main__":
    print ("Welcome to the quiz game!")
    try:
        difficulty = input("Please select a difficulty level (easy, medium, hard): ").lower()
        difficulty = difficulty.strip()
        if difficulty not in ["easy", "medium", "hard"]:
            raise ValueError
    except ValueError:
        print("Invalid input. Please try again.")
        exit()

    #create an empty list to hold the question objects
    question_bank = []
    for text in data.question_data:
        if text["difficulty"] == difficulty:
            #append the question_bank list with objects of the Question class
            question_bank.append(question_model.Question(text["question"], text["correct_answer"]))
              
    quiz = qb.QuizBrain(question_bank)
    while quiz.still_has_questions():
        if quiz.next_question():

            #increment the score if the answer is correct
            quiz.score += 1

    #print the final score
    print(f"You've completed the quiz!", 
          f"Your final score was: {quiz.score}/{len(quiz.question_list)}", 
          sep="\n")

