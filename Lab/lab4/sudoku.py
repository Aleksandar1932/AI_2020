from constraint import *


def read_solver():
    solver = input()
    if solver == "BacktrackingSolver":
        return Problem(BacktrackingSolver())
    elif solver == "RecursiveBacktrackingSolver":
        return Problem(RecursiveBacktrackingSolver())
    elif solver == "MinConflictsSolver":
        return Problem(MinConflictsSolver())


if __name__ == '__main__':
    problem = read_solver()

    variables = range(0, 81)  # 81 fields
    domain = range(1, 10)  # 1 - 9 values for each field
    problem.addVariables(variables, domain)

    # AllDifferent in row:
    for row in range(0, 9):
        problem.addConstraint(AllDifferentConstraint(), [(row * 9 + el) for el in range(0, 9)])

    # AllDifferent in column:
    for column in range(0, 9):
        problem.addConstraint(AllDifferentConstraint(), [(el * 9 + column) for el in range(0, 9)])

    # AllDifferent in block:
    for v_delimiter in range(0, 9, 3):
        for h_delimiter in range(0, 9, 3):
            problem.addConstraint(AllDifferentConstraint(),
                                  [((y * 9) + x) for x in range(h_delimiter, h_delimiter + 3) for y in
                                   range(v_delimiter, v_delimiter + 3)])

    solution = problem.getSolution()
    print(solution)
