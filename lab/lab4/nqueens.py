from constraint import *

if __name__ == '__main__':
    n = int(input())

    problem = Problem(BacktrackingSolver())

    queens = range(1, n + 1)
    domain = [(i, j) for i in range(0, n) for j in range(0, n)]

    problem.addVariables(queens, domain)

    # Constraints
    for queen1 in queens:
        for queen2 in queens:
            if queen1 < queen2:
                problem.addConstraint(lambda q1, q2:
                                      q1[0] != q2[0]  # row
                                      and q1[1] != q2[1]  # column
                                      and (q1[1] - q1[0]) != (q2[1] - q2[0])  # diagonally \
                                      and (q1[1] + q1[0]) != (q2[1] + q2[0]), (queen1, queen2))  # diagonally /

    if n <= 6:
        print(len(problem.getSolutions()))
    else:
        print(problem.getSolution())
