import requests
import random
import html
#Education-Focused Category(General-Knowledge, Science & History)
SPORTS_ID=21
API_URL=f"https://opentdb.com/api.php?amount=10&category={SPORTS_ID}&type=multiple"
#Get the questions
def get_sports_questions():
    response=requests.get(API_URL)
    #Checking the response code
    if response.status_code==200:
        data=response.json()
        if data['response_code']==0 and data['results']:
            return data['results']
    return None
def run_quiz():
    questions=get_sports_questions()
    if not questions:
        print("Failed to fetch questions")
        return 
    score=0
    print('Welcome to the Sports Trivia\n')
    for i, q in enumerate(questions,1):
        question=html.unescape(q['question'])
        correct=html.unescape(q['correct_answer'])
        incorrects=[html.unescape(a) for a in q['incorrect_answers']]
        #Shuffle the answers
        options=incorrects+[correct]
        random.shuffle(options)
        #Display the question
        print(f"Question {i}:{question}")
        for idx, option in enumerate(options,1):
            print(f"{idx}. {option}")
        #Validate the answer
        while True:
            try:
                choice=int(input("\nYour Answer (1-4):"))
                if 1<=choice<=4:
                    break
            except ValueError:
                pass
            print("Invalid Input")
        #Check the answer
        if options[choice-1]==correct:
            print("✅\nCorrect!\n")
            score+=1
        else:
            print(f"❌\nWrong!\n Correct answer: {correct}\n")
    print(f"Percentage Score:{score/len(questions)*100:1f}%")
run_quiz()
