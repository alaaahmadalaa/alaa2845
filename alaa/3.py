import json


def load_questions_from_json_file(file_path):
    with open(file_path, 'r') as file:
        questions = json.load(file)
        return questions

# The administer_quiz function remains the same as in the text file example


questions_file = "questions.json"
user_name = input("Enter your name: ")
quiz_questions = load_questions_from_json_file(questions_file)
user_score = administer_quiz(quiz_questions)

print(f"Dear {user_name}, your score is: {user_score}/20")

with open("user_results.json", "a") as result_file:
    result_file.write(json.dumps({user_name: user_score}) + "\n")
