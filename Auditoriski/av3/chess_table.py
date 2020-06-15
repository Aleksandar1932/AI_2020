from Auditoriski.av3.utils import Problem
from Auditoriski.av3.uninformed_search import *


def k1(x, y, b_x, b_y):  # up up left
    if 0 < x - 1 < 8 and 0 < y + 2 < 8 and [x - 1, y + 2] != [b_x, b_y]:
        x -= 1
        y += 2
    return x, y


def k2(x, y, b_x, b_y):  # up up right
    if 0 < x + 1 < 8 and 0 < y + 2 < 8 and [x + 1, y + 2] != [b_x, b_y]:
        x += 1
        y += 2
    return x, y


def k3(x, y, b_x, b_y):  # right right up
    if 0 < x + 2 < 8 and 0 < y + 1 < 8 and [x + 2, y + 1] != [b_x, b_y]:
        x += 2
        y += 1
    return x, y


def k4(x, y, b_x, b_y):  # right right down
    if 0 < x + 2 < 8 and 0 < y - 1 < 8 and [x + 2, y - 1] != [b_x, b_y]:
        x += 2
        y -= 1
    return x, y


def k5(x, y, b_x, b_y):  # down down right
    if 0 < x + 1 < 8 and 0 < y - 2 < 8 and [x + 1, y - 2] != [b_x, b_y]:
        x += 1
        y -= 2
    return x, y


def k6(x, y, b_x, b_y):  # down down left
    if 0 < x - 1 < 8 and 0 < y - 2 < 8 and [x - 1, y - 2] != [b_x, b_y]:
        x -= 1
        y -= 2
    return x, y


def k7(x, y, b_x, b_y):  # left left down
    if 0 < x - 2 < 8 and 0 < y - 1 < 8 and [x - 2, y - 1] != [b_x, b_y]:
        x -= 2
        y -= 1
    return x, y


def k8(x, y, b_x, b_y):  # left left up
    if 0 < x - 2 < 8 and 0 < y + 1 < 8 and [x - 2, y + 1] != [b_x, b_y]:
        x -= 2
        y += 1
    return x, y


def b1(x, y, k_x, k_y):  # up left
    if 0 < x - 1 < 8 and 0 < y + 1 < 8 and [x - 1, y + 1] != [k_x, k_y]:
        x -= 1
        y += 1
    return x, y


def b2(x, y, k_x, k_y):  # up right
    if 0 < x + 1 < 8 and 0 < y + 1 < 8 and [x + 1, y + 1] != [k_x, k_y]:
        x += 1
        y += 1
    return x, y


def b3(x, y, k_x, k_y):  # down left
    if 0 < x - 1 < 8 and 0 < y - 1 < 8 and [x - 1, y - 1] != [k_x, k_y]:
        x -= 1
        y -= 1
    return x, y


def b4(x, y, k_x, k_y):  # down right
    if 0 < x + 1 < 8 and 0 < y - 1 < 8 and [x + 1, y - 1] != [k_x, k_y]:
        x += 1
        y -= 1
    return x, y


class Stars(Problem):
    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)

    def successor(self, state):
        successors = dict()

        knight_x = state[0]
        knight_y = state[1]

        bishop_x = state[2]
        bishop_y = state[3]

        stars_positions = state[4]

        new_x, new_y = k1(knight_x, knight_y, bishop_x, bishop_y)
        if (knight_x, knight_y) != (new_x, new_y):
            successors['K1'] = (new_x, new_y,
                                bishop_x, bishop_y,
                                tuple([s for s in stars_positions if s[0] != new_x or s[1] != new_y])  # eat star if
                                # possible
                                )

        new_x, new_y = k2(knight_x, knight_y, bishop_x, bishop_y)
        if (knight_x, knight_y) != (new_x, new_y):
            successors['K2'] = (new_x, new_y,
                                bishop_x, bishop_y,
                                tuple([s for s in stars_positions if s[0] != new_x or s[1] != new_y])  # eat star if
                                # possible
                                )

        new_x, new_y = k3(knight_x, knight_y, bishop_x, bishop_y)
        if (knight_x, knight_y) != (new_x, new_y):
            successors['K3'] = (new_x, new_y,
                                bishop_x, bishop_y,
                                tuple([s for s in stars_positions if s[0] != new_x or s[1] != new_y])  # eat star if
                                # possible
                                )

        new_x, new_y = k4(knight_x, knight_y, bishop_x, bishop_y)
        if (knight_x, knight_y) != (new_x, new_y):
            successors['K4'] = (new_x, new_y,
                                bishop_x, bishop_y,
                                tuple([s for s in stars_positions if s[0] != new_x or s[1] != new_y])  # eat star if
                                # possible
                                )

        new_x, new_y = k5(knight_x, knight_y, bishop_x, bishop_y)
        if (knight_x, knight_y) != (new_x, new_y):
            successors['K5'] = (new_x, new_y,
                                bishop_x, bishop_y,
                                tuple([s for s in stars_positions if s[0] != new_x or s[1] != new_y])  # eat star if
                                # possible
                                )

        new_x, new_y = k6(knight_x, knight_y, bishop_x, bishop_y)
        if (knight_x, knight_y) != (new_x, new_y):
            successors['K6'] = (new_x, new_y,
                                bishop_x, bishop_y,
                                tuple([s for s in stars_positions if s[0] != new_x or s[1] != new_y])  # eat star if
                                # possible
                                )

        new_x, new_y = k7(knight_x, knight_y, bishop_x, bishop_y)
        if (knight_x, knight_y) != (new_x, new_y):
            successors['K7'] = (new_x, new_y,
                                bishop_x, bishop_y,
                                tuple([s for s in stars_positions if s[0] != new_x or s[1] != new_y])  # eat star if
                                # possible
                                )

        new_x, new_y = k8(knight_x, knight_y, bishop_x, bishop_y)
        if (knight_x, knight_y) != (new_x, new_y):
            successors['K8'] = (new_x, new_y,
                                bishop_x, bishop_y,
                                tuple([s for s in stars_positions if s[0] != new_x or s[1] != new_y])  # eat star if
                                # possible
                                )

        new_x, new_y = b1(bishop_x, bishop_y, knight_x, knight_y)
        if (bishop_x, bishop_y) != (new_x, new_y):
            successors['B1'] = (knight_x, knight_y, new_x, new_y,
                                tuple([s for s in stars_positions if s[0] != new_x or s[1] != new_y])
                                )

        new_x, new_y = b2(bishop_x, bishop_y, knight_x, knight_y)
        if (bishop_x, bishop_y) != (new_x, new_y):
            successors['B2'] = (knight_x, knight_y, new_x, new_y,
                                tuple([s for s in stars_positions if s[0] != new_x or s[1] != new_y])
                                )

        new_x, new_y = b3(bishop_x, bishop_y, knight_x, knight_y)
        if (bishop_x, bishop_y) != (new_x, new_y):
            successors['B3'] = (knight_x, knight_y, new_x, new_y,
                                tuple([s for s in stars_positions if s[0] != new_x or s[1] != new_y])
                                )

        new_x, new_y = b4(bishop_x, bishop_y, knight_x, knight_y)
        if (bishop_x, bishop_y) != (new_x, new_y):
            successors['B4'] = (knight_x, knight_y, new_x, new_y,
                                tuple([s for s in stars_positions if s[0] != new_x or s[1] != new_y])
                                )

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return len(state[-1]) == 0


if __name__ == '__main__':
    knight = [2, 5]
    bishop = [5, 1]
    stars_pos = ((1, 1), (4, 3), (6, 6))

    stars = Stars((knight[0], knight[1], bishop[0], bishop[1], stars_pos))

    result = breadth_first_graph_search(stars)
    print(result.solution())
