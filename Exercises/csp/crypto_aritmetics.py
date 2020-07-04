from constraint import *
from constraint import MinConflictsSolver


def get_letters(ws):
    """Funkcija koja kako vlez prima zborovi, a vraka set od bukvite koi se srekavaat vo zborovite"""
    words_set = set()

    for word in ws:
        for letter in word:
            words_set.add(letter)

    return list(words_set)


def letters_constraint(*args):
    nums = args
    letters = get_letters(words + word_solution)

    letters_nums = dict(zip(letters, nums))

    word_solution_num = word_to_num(word_solution, letters_nums)
    words_nums = []

    for w in words:
        words_nums.append(word_to_num([w], letters_nums))

    retval = False

    if sum(words_nums) == word_solution_num:
        retval = True

    for w in words + word_solution:
        if letters_nums[w[0]] == 0:
            retval = False

    return retval


def word_to_num(word, letters_dict):
    ret_num = 0

    for (i, letter) in enumerate(word[0]):
        ret_num += 10 ** (len(word[0]) - i) * letters_dict[letter]

    return ret_num


def get_leftmost_digit(number_string):
    return int(number_string[0])


if __name__ == '__main__':
    words = ["SEND", "MORE"]
    word_solution = ["MONEY"]

    # Init problem
    problem = Problem(BacktrackingSolver())

    # Init variables and domain and add them to the problem
    variables = get_letters(words + word_solution)
    domain = range(0, 10)
    problem.addVariables(variables, domain)

    problem.addConstraint(letters_constraint, variables)

    print(problem.getSolution())
