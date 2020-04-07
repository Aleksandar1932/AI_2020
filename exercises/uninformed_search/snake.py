from abc import ABC

from searching_framework.uninformed_search import *
from searching_framework.utils import *

"""
    zmija : tuple od koordinati
    orientacija na zmija:
            N
        W       E
            S
    zeleni_jabolki: tuple od koordinati
    crveni_jabolki: tuple od koordinati
    
"""


def move_snake_down(snake, zeleni_jabolki, crveni_jabolki):
    # podvizuvaje dolu y - 1
    snake_list = list(list(coord) for coord in snake)
    crveni_jabolki_list = list(list(coord) for coord in crveni_jabolki)
    zeleni_jabolki_list = list(list(coord) for coord in zeleni_jabolki)

    curr_head = snake_list[-1]
    if curr_head[1] - 1 >= 0 and [curr_head[0], curr_head[1] - 1] not in crveni_jabolki_list:
        new_head = [curr_head[0], curr_head[1] - 1]
        snake_list.append(new_head)

        if snake_list[-1] not in zeleni_jabolki_list:
            del snake_list[0]
        else:
            zeleni_jabolki_list = [coord for coord in zeleni_jabolki_list if coord != [snake_list[-1]]]

    return tuple(tuple(coord) for coord in snake_list), tuple(tuple(coord) for coord in zeleni_jabolki_list), tuple(
        tuple(coord) for coord in crveni_jabolki)


def move_snake_up(snake, zeleni_jabolki, crveni_jabolki):
    # podvizuvaje dolu y + 1
    snake_list = list(list(coord) for coord in snake)
    crveni_jabolki_list = list(list(coord) for coord in crveni_jabolki)
    zeleni_jabolki_list = list(list(coord) for coord in zeleni_jabolki)

    curr_head = snake_list[-1]
    if curr_head[1] + 1 <= 9 and [curr_head[0], curr_head[1] + 1] not in crveni_jabolki_list:
        new_head = [curr_head[0], curr_head[1] + 1]
        snake_list.append(new_head)

        if snake_list[-1] not in zeleni_jabolki_list:
            del snake_list[0]
        else:
            zeleni_jabolki_list = [coord for coord in zeleni_jabolki_list if coord != [snake_list[-1]]]

    return tuple(tuple(coord) for coord in snake_list), tuple(tuple(coord) for coord in zeleni_jabolki_list), tuple(
        tuple(coord) for coord in crveni_jabolki)


def move_snake_left(snake, zeleni_jabolki, crveni_jabolki):
    # podvizuvaje dolu x - 1
    snake_list = list(list(coord) for coord in snake)
    crveni_jabolki_list = list(list(coord) for coord in crveni_jabolki)
    zeleni_jabolki_list = list(list(coord) for coord in zeleni_jabolki)

    curr_head = snake_list[-1]
    if curr_head[0] - 1 >= 0 and [curr_head[0] - 1, curr_head[1]] not in crveni_jabolki_list:
        new_head = [curr_head[0] - 1, curr_head[1]]
        snake_list.append(new_head)

        if snake_list[-1] not in zeleni_jabolki_list:
            del snake_list[0]
        else:
            zeleni_jabolki_list = [coord for coord in zeleni_jabolki_list if coord != [snake_list[-1]]]

    return tuple(tuple(coord) for coord in snake_list), tuple(tuple(coord) for coord in zeleni_jabolki_list), tuple(
        tuple(coord) for coord in crveni_jabolki)


def move_snake_right(snake, zeleni_jabolki, crveni_jabolki):
    # podvizuvaje dolu x + 1
    snake_list = list(list(coord) for coord in snake)
    crveni_jabolki_list = list(list(coord) for coord in crveni_jabolki)
    zeleni_jabolki_list = list(list(coord) for coord in zeleni_jabolki)

    curr_head = snake_list[-1]
    if curr_head[0] + 1 <= 9 and [curr_head[0] + 1, curr_head[1]] not in crveni_jabolki_list:
        new_head = [curr_head[0] + 1, curr_head[1]]
        snake_list.append(new_head)

        if snake_list[-1] not in zeleni_jabolki_list:
            del snake_list[0]
        else:
            zeleni_jabolki_list = [coord for coord in zeleni_jabolki_list if coord != [snake_list[-1]]]

    return tuple(tuple(coord) for coord in snake_list), tuple(tuple(coord) for coord in zeleni_jabolki_list), tuple(
        tuple(coord) for coord in crveni_jabolki)


class Snake(Problem, ABC):

    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)

    def successor(self, state):
        successors = {}
        curr_snake = state[0]
        curr_orientation = state[1]
        curr_zeleni = state[2]
        curr_crveni = state[3]

        # ProdolzhiPravo
        # orientacija: S -> dvizenje dolu
        if curr_orientation == "S":
            new_orientation = curr_orientation
            new_snake, new_zeleni, new_crveni = move_snake_down(curr_snake, curr_zeleni, curr_crveni)
            if new_snake != curr_snake:
                successors["ProdolzhiPravo"] = (new_snake, new_orientation, new_zeleni, new_crveni)

        # orientacija: N -> dvizenje gore
        if curr_orientation == "N":
            new_orientation = curr_orientation
            new_snake, new_zeleni, new_crveni = move_snake_up(curr_snake, curr_zeleni, curr_crveni)
            if new_snake != curr_snake:
                successors["ProdolzhiPravo"] = (new_snake, new_orientation, new_zeleni, new_crveni)

        # orientacija: W -> dvizenje levo
        if curr_orientation == "W":
            new_orientation = curr_orientation
            new_snake, new_zeleni, new_crveni = move_snake_left(curr_snake, curr_zeleni, curr_crveni)
            if new_snake != curr_snake:
                successors["ProdolzhiPravo"] = (new_snake, new_orientation, new_zeleni, new_crveni)

        # orientacija: E -> dvizenje desno
        if curr_orientation == "E":
            new_orientation = curr_orientation
            new_snake, new_zeleni, new_crveni = move_snake_right(curr_snake, curr_zeleni, curr_crveni)
            if new_snake != curr_snake:
                successors["ProdolzhiPravo"] = (new_snake, new_orientation, new_zeleni, new_crveni)

        # SvrtiDesno
        # orientacija: S -> dvizenje levo
        if curr_orientation == "S":
            new_orientation = "W"
            new_snake, new_zeleni, new_crveni = move_snake_left(curr_snake, curr_zeleni, curr_crveni)
            if new_snake != curr_snake:
                successors["SvrtiDesno"] = (new_snake, new_orientation, new_zeleni, new_crveni)

        # orientacija: N -> dvizenje desno
        if curr_orientation == "N":
            new_orientation = "E"
            new_snake, new_zeleni, new_crveni = move_snake_right(curr_snake, curr_zeleni, curr_crveni)
            if new_snake != curr_snake:
                successors["SvrtiDesno"] = (new_snake, new_orientation, new_zeleni, new_crveni)

        # orientacija: W -> dvizenje gore
        if curr_orientation == "W":
            new_orientation = "N"
            new_snake, new_zeleni, new_crveni = move_snake_up(curr_snake, curr_zeleni, curr_crveni)
            if new_snake != curr_snake:
                successors["SvrtiDesno"] = (new_snake, new_orientation, new_zeleni, new_crveni)

        # orientacija: E -> dvizenje dolu
        if curr_orientation == "E":
            new_orientation = "S"
            new_snake, new_zeleni, new_crveni = move_snake_down(curr_snake, curr_zeleni, curr_crveni)
            if new_snake != curr_snake:
                successors["SvrtiDesno"] = (new_snake, new_orientation, new_zeleni, new_crveni)

        # SvrtiLevo
        # orientacija: S -> dvizenje desno
        if curr_orientation == "S":
            new_orientation = "E"
            new_snake, new_zeleni, new_crveni = move_snake_right(curr_snake, curr_zeleni, curr_crveni)
            if new_snake != curr_snake:
                successors["SvrtiLevo"] = (new_snake, new_orientation, new_zeleni, new_crveni)

        # orientacija: N -> dvizenje levo
        if curr_orientation == "N":
            new_orientation = "W"
            new_snake, new_zeleni, new_crveni = move_snake_left(curr_snake, curr_zeleni, curr_crveni)
            if new_snake != curr_snake:
                successors["SvrtiLevo"] = (new_snake, new_orientation, new_zeleni, new_crveni)

        # orientacija: W -> dvizenje dolu
        if curr_orientation == "W":
            new_orientation = "S"
            new_snake, new_zeleni, new_crveni = move_snake_down(curr_snake, curr_zeleni, curr_crveni)
            if new_snake != curr_snake:
                successors["SvrtiLevo"] = (new_snake, new_orientation, new_zeleni, new_crveni)

        # orientacija: E -> dvizenje gore
        if curr_orientation == "E":
            new_orientation = "N"
            new_snake, new_zeleni, new_crveni = move_snake_up(curr_snake, curr_zeleni, curr_crveni)
            if new_snake != curr_snake:
                successors["SvrtiLevo"] = (new_snake, new_orientation, new_zeleni, new_crveni)

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return len(state[2]) == 0


if __name__ == '__main__':
    n = int(input())
    zeleni_jabolki = tuple(tuple(map(int, input().split(','))) for _ in range(n))
    m = int(input())
    crveni_jabolki = tuple(tuple(map(int, input().split(','))) for _ in range(m))

    snake_initial = ((0, 9), (0, 8), (0, 7))
    snake_orientation = "S"

    state_initial = (snake_initial, snake_orientation, zeleni_jabolki, crveni_jabolki)

    snake_problem = Snake(state_initial)

    print(depth_first_graph_search(snake_problem).solution())
