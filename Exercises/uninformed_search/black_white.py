"""
Potrebata za revisit na ovaa zadacha e poradi vezbanje za prviot del od junskiot ispit
"""
from searching_framework import *


def inverse_bit(bit_to_inv):
	if bit_to_inv == 0:
		return 1
	return 0


def pick_point(position, state):
	state_n = len(state[0])
	# position: (row, col)
	pos_up = (position[0], position[1] - 1)
	pos_down = (position[0], position[1] + 1)
	pos_left = (position[0] - 1, position[1])
	pos_right = (position[0] + 1, position[1])

	positions_proposed = [position, pos_up, pos_down, pos_left, pos_right]
	positions = []
	for (i, pos) in enumerate(positions_proposed):
		if not (pos[0] < 0 or pos[0] >= state_n) and not (pos[1] < 0 or pos[1] >= state_n):
			positions.append(pos)

	state_list = [list(row) for row in state]

	for pos in positions:
		r = pos[0]
		c = pos[1]

		state_list[r][c] = inverse_bit(state_list[r][c])

	return tuple((tuple(row) for row in state_list))


class BlackWhite(Problem):
	def __init__(self, initial, goal):
		super().__init__(initial, goal)

	def successor(self, state):
		successors = {}
		for row_ind in range(0, len(state[0])):
			for column_ind in range(0, len(state[0])):
				new_state = pick_point((row_ind, column_ind), state)
				if new_state != state:
					successors["x: {}, y: {}".format(row_ind, column_ind)] = new_state
		return successors

	def actions(self, state):
		return self.successor(state).keys()

	def result(self, state, action):
		return self.successor(state)[action]

	def goal_test(self, state):
		return state == self.goal


def generate_state(fields_list, n):
	return tuple(zip(*(iter(fields_list),) * n))


def generate_goal(n):
	return generate_state([1] * n ** 2, n)


if __name__ == '__main__':
	n = int(input())
	fields = list(map(int, input().split(',')))

	bw_problem = BlackWhite(
		generate_state(fields, n),  # initial state generated from input `fields`
		generate_goal(n)  # goal state
	)

	solution = breadth_first_graph_search(bw_problem)
	print(solution.solution())
