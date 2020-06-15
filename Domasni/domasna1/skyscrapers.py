from constraint import *


def get_visibility(skyscrapers_array):
    for i in range(0, len(skyscrapers_array)):
        for j in range(i, len(skyscrapers_array)):
            if skyscrapers_array[j] < skyscrapers_array[i]:
                skyscrapers_array[j] = 0
    return len([sk for sk in skyscrapers_array if sk != 0])


def check_visibility(expected_visibility, skyscrapers_array):
    return expected_visibility == get_visibility(skyscrapers_array)


if __name__ == '__main__':
    n = int(input())
    columns_top = (2, 1, 2, 2)
    columns_bottom = (2, 4, 3, 1)
    rows_left = (2, 3, 1, 2)
    rows_right = (2, 2, 3, 1)

    problem = Problem()
    variables = [(i, j) for i in range(0, n) for j in range(0, n)]
    domain = range(1, n + 1)
    problem.addVariables(variables, domain)

    # Adding Constraints
    for row in range(0, n):
        current_row = [coord for coord in variables if coord[0] == row]
        problem.addConstraint(AllDifferentConstraint(), current_row)
        problem.addConstraint(check_visibility, (rows_left[row], current_row))
        problem.addConstraint(check_visibility, (rows_right[row], current_row[::-1]))

    for column in range(0, n):
        current_column = [coord for coord in variables if coord[1] == column]
        problem.addConstraint(AllDifferentConstraint(), current_column)
        problem.addConstraint(check_visibility, (columns_top[column], current_column))
        problem.addConstraint(check_visibility, (columns_bottom[column], current_column[::-1]))
        # problem.addConstraint(lambda c: columns_top[column] == get_visibility(c), tuple(current_column))
        # problem.addConstraint(lambda c: columns_bottom[column] == get_visibility(c), tuple(current_column[::-1]))

    print(problem.getSolution())
