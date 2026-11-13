
questions = [
    {
        "question": "Which language are we learning?",
        "options": ["Java", "Python", "C++", "PHP"],
        "answer": "B"
    },
    {
        "question": "Which function displays output in Python?",
        "options": ["input()", "print()", "output()", "show()"],
        "answer": "B"
    },
    {
        "question": "Which data type stores True or False?",
        "options": ["String", "Integer", "Boolean", "Float"],
        "answer": "C"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["//", "#", "/*", "&"],
        "answer": "B"
    },
    {
        "question": "Which keyword is used to create a function?",
        "options": ["function", "define", "def", "fun"],
        "answer": "C"
    }
]

score = 0

print("\n====== Quiz Management System ======")
print("Welcome to the Python Quiz!")
print("There are", len(questions), "questions.")
print("Each correct answer gives 1 point.")

name = input("\nEnter your name: ")

for i, question in enumerate(questions, start=1):

    print("\nQuestion", i)
    print(question["question"])

    options = ["A", "B", "C", "D"]

    for j, option in enumerate(question["options"]):
        print(options[j] + ".", option)

    answer = input("Enter your answer (A/B/C/D): ").upper()

    if answer not in options:
        print("Invalid answer!")
        continue

    if answer == question["answer"]:
        print("Correct answer!")
        score += 1
    else:
        print("Wrong answer!")
        print("Correct answer:", question["answer"])

print("\n====== Quiz Result ======")
print("Student Name:", name)
print("Total Questions:", len(questions))
print("Correct Answers:", score)
print("Wrong Answers:", len(questions) - score)
print("Final Score:", score, "/", len(questions))

percentage = (score / len(questions)) * 100

print("Percentage:", percentage, "%")

if percentage >= 80:
    print("Excellent performance!")

elif percentage >= 50:
    print("Good job! Keep practicing.")

else:
    print("Keep learning and try again!")

print("\nThank you for playing!")
