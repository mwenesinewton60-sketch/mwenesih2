questions = [
    "What is the capital of France?",
    "What is 5 + 7?",
    "What is the largest planet in our solar system?",
    "Who wrote 'Romeo and Juliet'?",
    "What is the boiling point of water in Celsius?"
]

answers = [
    "paris",
    "12",
    "jupiter",
    "shakespeare",
    "100"
]

score = 0

for i in range(len(questions)):
    print("\nQuestion", i + 1, ":", questions[i])
    user_answer = input("Your answer: ").lower().strip()

    if user_answer == answers[i]:
        print("Correct!")
        score += 1
    else:
        print("Wrong! The correct answer was:", answers[i])

print("\n--- QUIZ FINISHED ---")
print("Your score:", score, "out of", len(questions))