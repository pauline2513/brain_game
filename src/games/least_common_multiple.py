import random
import math


def least_common_multiple():
    first_number = random.randint(10, 100)
    second_number = random.randint(10, 100)
    third_number = random.randint(10, 100)
    lcm_first_second = ((first_number * second_number) //
                        math.gcd(first_number, second_number))
    lcm_answer = ((lcm_first_second * third_number) //
                  math.gcd(lcm_first_second, third_number))
    question_line = ' '.join([str(first_number),
                              str(second_number),
                              str(third_number)])
    return question_line, lcm_answer
