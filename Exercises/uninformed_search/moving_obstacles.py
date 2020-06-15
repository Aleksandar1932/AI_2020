"""
    obstacle1: 2,8 3,8 levo
        possible {levo, desno}
    obstacle2: 2,2 3,2 2,3 3,3 gd
        possible {gd, dl}
"""
from searching_framework.uninformed_search import *
from searching_framework.utils import *


def move_ob1(ob):
    ob_list = list(el for el in ob)

    x1 = ob_list[0]
    x2 = ob_list[2]
    dir = ob_list[4]

    if dir == "levo":
        if x1 == 0:
            ob_list[4] = "desno"
            ob_list[0] += 1
            ob_list[2] += 1
        else:
            ob_list[0] -= 1
            ob_list[2] -= 1
    elif dir == "desno":
        if x2 == 5:
            ob_list[4] = "levo"
            ob_list[0] -= 1
            ob_list[2] -= 1
        else:
            ob_list[0] += 1
            ob_list[2] += 1

    return tuple(el for el in ob_list)


def move_ob2(ob):
    ob_list = list(el for el in ob)
    dir = ob_list[8]

    if dir == "gd":
        if (ob_list[6], ob_list[7]) == (5, 5):
            ob_list[8] = "dl"
            for i in range(0, 8): ob_list[i] -= 1
        else:
            for i in range(0, 8): ob_list[i] += 1

    elif dir == "dl":
        if (ob_list[0], ob_list[1]) == (0, 0):
            ob_list[8] = "gd"
            for i in range(0, 8): ob_list[i] += 1
        else:
            for i in range(0, 8): ob_list[i] -= 1

    return tuple(el for el in ob_list)


def move_ob3(ob):
    ob_list = list(el for el in ob)
    y1 = ob_list[1]
    y2 = ob_list[3]
    dir = ob_list[4]

    if dir == "dolu":
        if y1 == 0:
            ob_list[4] = "gore"
            ob_list[1] += 1
            ob_list[3] += 1
        else:
            ob_list[1] -= 1
            ob_list[3] -= 1

    elif dir == "gore":
        if y2 == 5:
            ob_list[4] = "dolu"
            ob_list[1] -= 1
            ob_list[3] -= 1
        else:
            ob_list[1] += 1
            ob_list[3] += 1
    return tuple(el for el in ob_list)


class Explorer(Problem):

    def __init__(self, initial, goal):
        super().__init__(initial, goal)

    def successor(self, state):
        successors = {}

        m_x = state[0]
        m_y = state[1]

        moved_ob1 = move_ob1(state[2])
        moved_ob2 = move_ob2(state[3])
        moved_ob3 = move_ob3(state[4])

        obstacles_coords = [
            [moved_ob1[0], moved_ob1[1]],
            [moved_ob1[2], moved_ob1[3]],

            [moved_ob2[0], moved_ob2[1]],
            [moved_ob2[2], moved_ob2[3]],
            [moved_ob2[4], moved_ob2[5]],
            [moved_ob2[6], moved_ob2[7]],

            [moved_ob3[0], moved_ob3[1]],
            [moved_ob3[2], moved_ob3[3]]
        ]

        # right
        new_x = m_x + 1
        new_y = m_y

        if not (new_x >= 6 and new_y >= 6) and [new_x, new_y] not in obstacles_coords and new_x <= 10:
            successors["Desno"] = (new_x, new_y, moved_ob1, moved_ob2, moved_ob3)

        # left
        new_x = m_x - 1
        new_y = m_y
        if new_x >= 0 and [new_x, new_y] not in obstacles_coords:
            successors["Levo"] = (new_x, new_y, moved_ob1, moved_ob2, moved_ob3)

        # up
        new_x = m_x
        new_y = m_y + 1

        if not (new_x >= 6 and new_y >= 6) and [new_x, new_y] not in obstacles_coords and new_y <= 10:
            successors["Gore"] = (new_x, new_y, moved_ob1, moved_ob2, moved_ob3)

        # down
        new_x = m_x
        new_y = m_y - 1

        if new_y >= 0 and [new_x, new_y] not in obstacles_coords:
            successors["Dolu"] = (new_x, new_y, moved_ob1, moved_ob2, moved_ob3)

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return (state[0], state[1]) == (self.goal[0], self.goal[1])


if __name__ == '__main__':
    ob1 = (2, 8, 3, 8, "levo")
    ob2 = (2, 2, 3, 2, 2, 3, 3, 3, "gd")
    ob3 = (8, 2, 8, 3, "dolu")

    man_x = int(input())
    man_y = int(input())
    house_x = int(input())
    house_y = int(input())

    initial_state = (man_x, man_y, ob1, ob2, ob3)
    goal_state = (house_x, house_y)

    explorer_problem = Explorer(initial_state, goal_state)

    print(breadth_first_graph_search(explorer_problem).solution())
