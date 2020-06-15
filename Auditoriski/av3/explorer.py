from Auditoriski.av3.utils import Problem
from Auditoriski.av3.uninformed_search import *


def check_obstacle(obstacle, max_y):
    if obstacle[2] == 0:  # up
        if obstacle[1] == max_y - 1:
            obstacle[2] = 1
            obstacle[1] -= 1
        else:
            obstacle[1] += 1
    else:
        if obstacle[1] == 0:
            obstacle[2] = 0
            obstacle[1] += 1
        else:
            obstacle[1] -= 1

    return obstacle


class Explorer(Problem):
    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)
        self.grid_size = [8, 6]

    def successor(self, state):
        successors = {}  # inicijaliziranje na prazen recnik

        man_x = state[0]
        man_y = state[1]

        obstacle1 = [state[2], state[3], state[4]]  # (x, y, DIRECTION) 0 = up; 1 = down
        obstacle2 = [state[5], state[6], state[7]]  # (x, y, DIRECTION) 0 = up; 1 = down

        max_x = self.grid_size[0]
        max_y = self.grid_size[1]

        # if obstacle1[2] == 0:  # up
        #     if obstacle1[1] == max_y - 1:
        #         obstacle1[2] = 1
        #         obstacle1[1] -= 1
        #     else:
        #         obstacle1[1] += 1
        # else:
        #     if obstacle1[1] == 0:
        #         obstacle1[2] = 0
        #         obstacle1[1] += 1
        #     else:
        #         obstacle1[1] -= 1

        obstacle1 = check_obstacle(obstacle1, max_y)
        obstacle2 = check_obstacle(obstacle2, max_y)
        # if obstacle2[2] == 0:  # up
        #     if obstacle2[1] == max_y - 1:
        #         obstacle2[2] = 1
        #         obstacle2[1] -= 1
        #     else:
        #         obstacle2[1] += 1
        # else:
        #     if obstacle2[1] == 0:
        #         obstacle2[2] = 0
        #         obstacle2[1] += 1
        #     else:
        #         obstacle2[1] -= 1

        obstacles = [[obstacle1[0], obstacle1[1]], [obstacle2[0], obstacle2[1]]]  # koordinati na precki

        if man_x < max_x - 1 and [man_x + 1, man_y] not in obstacles:  # right
            successors['Right'] = (man_x + 1, man_y,
                                   obstacle1[0], obstacle1[1], obstacle1[2],
                                   obstacle2[0], obstacle2[1], obstacle2[2])

        if man_x > 0 and [man_x - 1, man_y] not in obstacles:  # left
            successors['Left'] = (man_x - 1, man_y,
                                  obstacle1[0], obstacle1[1], obstacle1[2],
                                  obstacle2[0], obstacle2[1], obstacle2[2])

        if man_y < max_y - 1 and [man_x, man_y + 1] not in obstacles:  # up
            successors['Up'] = (man_x, man_y + 1,
                                obstacle1[0], obstacle1[1], obstacle1[2],
                                obstacle2[0], obstacle2[1], obstacle2[2])

        if man_y > 0 and [man_x, man_y - 1] not in obstacles:  # down
            successors['Down'] = (man_x, man_y - 1,
                                  obstacle1[0], obstacle1[1], obstacle1[2],
                                  obstacle2[0], obstacle2[1], obstacle2[2])

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        position = (state[0], state[1])  # (x, y) koordinati na covece
        return position == self.goal


if __name__ == '__main__':
    goal_state = (7, 4)
    initial_state = (0, 2)
    obstacle_1 = (2, 5, 1)  # down
    obstacle_2 = (5, 0, 0)  # up

    explorer = Explorer((initial_state[0], initial_state[1],
                         obstacle_1[0], obstacle_1[1], obstacle_1[2],
                         obstacle_2[0], obstacle_2[1], obstacle_2[2]), goal_state)

    print("BFS Approach:")
    print(breadth_first_graph_search(explorer).solution())
    print(breadth_first_graph_search(explorer).solve())

    print("DFS Approach:")
    print(depth_first_graph_search(explorer).solution())
    print(depth_first_graph_search(explorer).solve())

