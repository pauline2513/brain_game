from src.games.geometric_progression import geometric_progression


MAX_ROUNDS = 3


def question_creation(game_name):
    question, correct_answer = game_name()
    if game_name == geometric_progression:
        print("What number is missing in the progression?")
    else:
        print("Find the smallest common multiple of given numbers.")
    print("Question:", question, sep=" ")
    return correct_answer


def run_game(game_name, name):
    round = 1
    while round <= MAX_ROUNDS:
        correct_answer = question_creation(game_name)
        users_answer = input("Your answer: ")
        if users_answer == str(correct_answer):
            print("Correct!")
        else:
            print(f'{users_answer} is wrong answer ;(.'
                  f'Correct answer was {correct_answer}.')
            print(f"Let's try again, {name}!")
        round += 1
