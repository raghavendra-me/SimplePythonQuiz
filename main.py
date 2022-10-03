import requests
# creating a quiz application

URL = "https://opentdb.com/api.php?amount=5&category=9&difficulty=easy&type=boolean"
api_response = requests.get(URL)
que_data = api_response.json()["results"]


def start_quiz():
    score = 0
    try:
        with open("highscore.txt", mode="r") as file:
            pass
    except:
        with open("highscore.txt", mode="w") as file:
            high_score = 0
    else:
        with open("highscore.txt", mode="r") as file:
            high_score = file.read()
            high_score = int(high_score)

    for item in que_data:
        question = item["question"]
        crct_answer = item["correct_answer"]
        print(question)
        user_answer = input("Answer: True/False ").title()
        if user_answer == crct_answer:
            print("Correct Answer\n")
            score += 1
        else:
            print("Wrong Answer\n")

    if score >= high_score:
        with open("highscore.txt", mode="w") as file:
            file.write(str(score))
        print(f"Hurrah Your made a high score of {score}")
    else:
        print(f"Your final score is  {score}")


start_quiz()




