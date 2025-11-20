score = 0

questions = [{
    "question": "What is the capital of India?",
    "options": ["A. Maharashtra", "B. Delhi", "C. Odisha", "D. Govandi"],
    "answer": "B"
},
{
    "question": "Which language is this quiz written in?",
    "options": ["A. Java", "B. C++", "C. Python", "D. Ruby"],
    "answer": "C"
},
{
    "question": "What is 5 + 7?",
    "options": ["A. 10", "B. 11", "C. 12", "D. 13"],
    "answer": "C"
}]

print("Welcome to the Quiz App!")

for i in range(len(questions)):
    q=questions[i]
    print("Q",i+1,":",q['question'])
    i+1
    for options in q['options']:
        print(options)
    ans=input("Your answer (A/B/C/D):")
    if ans==q['answer']:
        print("CORRECT!!!")
        score+=1
    else:
        print("WRONG :/  Correct answer is:",q["answer"])


print("Your final score:",score,"/",len(questions))