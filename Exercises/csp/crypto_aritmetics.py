from constraint import *


def get_letters(ws):
    """Get all the unique letters from the words and the solution (variables in the CSP)"""
    words_set = set()

    for word in ws:
        for letter in word:
            words_set.add(letter)

    return list(words_set)


def get_assigned_map(vars):
    """Get current assignments to letters as map for further checks"""
    return dict(zip(get_letters(WORDS + SOLUTION_WORD), vars))


def letters_constraint(*args):
    """Letters arithmetic validity checker"""
    letters_nums = get_assigned_map(args)

    word_solution_num = word_to_num(SOLUTION_WORD, letters_nums)
    words_nums = []

    for w in WORDS:
        words_nums.append(word_to_num([w], letters_nums))

    return sum(words_nums) == word_solution_num


def word_to_num(word, letters_dict):
    """Word converted to number according to current assignments to variables"""
    ret_num = 0

    for (i, letter) in enumerate(word[0]):
        ret_num += 10 ** (len(word[0]) - i) * letters_dict[letter]

    return ret_num


def leading_zeros(*args):
    """No leading zeros checker"""
    letters_nums = get_assigned_map(args)

    for w in WORDS + SOLUTION_WORD:
        if letters_nums[w[0]] == 0:
            return False
    return True


if __name__ == '__main__':
    # Init variables, could be read from `input()`
    WORDS = ["TAKE", "A", "CAKE"]
    SOLUTION_WORD = ["KATE"]

    # Init problem
    problem = Problem(BacktrackingSolver())

    # Init variables and domain and add them to the problem
    variables = get_letters(WORDS + SOLUTION_WORD)
    domain = range(0, 10)
    problem.addVariables(variables, domain)

    # Add constraints
    problem.addConstraint(letters_constraint, variables)
    problem.addConstraint(leading_zeros, variables)
    problem.addConstraint(AllDifferentConstraint(), variables)

    # Print solution
    print(problem.getSolution())
