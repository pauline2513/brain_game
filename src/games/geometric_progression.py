import random


def geometric_progression():
    progression_length = random.randint(5, 10)
    progression_common_ratio = random.randint(2, 10)
    progression_start_number = random.randint(1, 10)
    progression_missed_position = random.randint(1, progression_length) - 1
    progression_list = [(progression_start_number *
                         progression_common_ratio ** i)
                        for i in range(progression_length)]
    progression_answer = progression_list[progression_missed_position]
    progression_list[progression_missed_position] = "..."
    question_line = " ".join([str(element) for element in progression_list])
    print(question_line)
    return question_line, progression_answer


geometric_progression()
