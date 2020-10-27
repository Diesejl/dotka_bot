from random import choice


def make_list_of_answers(quiz_dict, right_answer, picture_quiz=False):
    if picture_quiz:
        list_of_answers = [right_answer]
        while len(list_of_answers) != 6:
            new_answer = choice(list(quiz_dict.keys()))
            if new_answer not in list_of_answers:
                list_of_answers.append(new_answer)
        list_of_answers.sort()
        return list_of_answers
    else:
        right_answer_item = quiz_dict.get(right_answer)
        list_of_answers = [right_answer_item]
        while len(list_of_answers) != 6:
            new_item = choice(list(quiz_dict.values()))
            if new_item not in list_of_answers:
                list_of_answers.append(new_item)
        list_of_answers.sort()
        return list_of_answers
