from constraint import *

if __name__ == '__main__':
    n = int(input())

    problem = Problem(BacktrackingSolver())

    horses = range(0, n)
    domain = [(i, j) for i in range(0, n) for j in range(0, n)]
    problem.addVariables(horses, domain)

    # Constraint AllDiff horses
    problem.addConstraint(AllDifferentConstraint(), horses)
    # Constraint (delta_x = 1 and delta_x = 2) or (delta_x = 2 and delta_y = 1)
    for horse1 in horses:
        for horse2 in horses:
            if horse1 < horse2:
                problem.addConstraint(lambda h1, h2: not ((abs(h1[0] - h2[0]) == 1 and abs(h1[1] - h2[1]) == 2)
                                                          or (abs(h1[0] - h2[0]) == 2 and abs(h1[1] - h2[1]) == 1)),
                                      (horse1, horse2))

    if n <= 4:
        print(len(problem.getSolutions()))
    else:
        print(problem.getSolution())
