from random import choice
from data.usa_state_capital import CAPITALS


def make_list_of_answers(quiz_dict, right_answer):
    list_of_answers = [right_answer]
    while len(list_of_answers) != 6:
        new_answer = choice(list(quiz_dict.keys()))
        if new_answer not in list_of_answers:
            list_of_answers.append(new_answer)
    list_of_answers.sort()
    return list_of_answers


def make_list_of_capitals(hidden_state):
    print(hidden_state)
    hidden_capital = CAPITALS.get(hidden_state)
    print(hidden_capital)
    list_of_capitals = [hidden_capital]
    while len(list_of_capitals) != 6:
        new_capital = choice(list(CAPITALS.values()))
        if new_capital not in list_of_capitals:
            list_of_capitals.append(new_capital)
    list_of_capitals.sort()
    return list_of_capitals
