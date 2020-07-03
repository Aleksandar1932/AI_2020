"""
8puzzle problem

    1   2   3
    4   5   6
    7   8   *

"""

from searching_framework import *

BLANK_FIELD = -1


def find_blank_coordinates(state):
    for i in range(0, len(state)):
        for j in range(0, len(state[0])):
            if state[i][j] == BLANK_FIELD:
                return (i, j)
    return None


def check_valid_coord(coord):
    BNDY_MAX = 2
    BNDY_MIN = 0

    x = coord[0]
    y = coord[1]

    if x > BNDY_MAX or x < BNDY_MIN or y > BNDY_MAX or y < BNDY_MIN:
        return False
    return True


def find_valid_movements_coords(blank_position):
    positions = []

    up = (blank_position[0] - 1, blank_position[1])
    if check_valid_coord(up):
        positions.append(up)

    down = (blank_position[0] + 1, blank_position[1])
    if check_valid_coord(down):
        positions.append(down)

    left = (blank_position[0], blank_position[1] - 1)
    if check_valid_coord(left):
        positions.append(left)

    right = (blank_position[0], blank_position[1] + 1)
    if check_valid_coord(right):
        positions.append(right)

    return positions


def move_to_blank(state, blank_position, field_position):
    state_list = [list(row) for row in state]
    state_list[blank_position[0]][blank_position[1]], state_list[field_position[0]][field_position[1]] = \
        state_list[field_position[0]][field_position[1]], state_list[blank_position[0]][blank_position[1]],
    return tuple([tuple(row) for row in state_list])


class Puzzle(Problem):
    def __init__(self, initial, goal):
        super().__init__(initial, goal)

    def successor(self, state):
        blank_position = find_blank_coordinates(state)
        successors = {}
        valid_movements = find_valid_movements_coords(blank_position)

        for movement in valid_movements:
            successors["Blank from {} to {}".format(blank_position, movement)] = move_to_blank(state, blank_position,
                                                                                               movement)
        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state == self.goal

    def h(self, node):
        wrong_placed_fields = 0
        flatten_state = sum(node.state, ())
        for field in flatten_state:
            if field != -1 and flatten_state.index(field) != field - 1:
                wrong_placed_fields += 1

        return wrong_placed_fields


if __name__ == '__main__':
    initial_state = ((BLANK_FIELD, 1, 3), (4, 2, 5), (7, 8, 6))
    goal_state = ((1, 2, 3), (4, 5, 6), (7, 8, BLANK_FIELD))

    puzzle = Puzzle(initial_state, goal_state)

    print("== Uninformed search ==")

    result_uninformed = breadth_first_graph_search(puzzle)
    print(result_uninformed.solution())

    print("== Informed search ==")

    result_informed = astar_search(puzzle)
    print(result_informed.solution())
