from random import randrange


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, position):
        if position == "left":
            self.x -= 1

        if position == "right":
            self.x += 1

        if position == "up":
            self.y -= 1

        if position == "down":
            self.y += 1

        print(f"[{self.x - 1}, {self.y - 1}]")  # -1 zaradi offsetot so !

    def get_coordinates(self, position):
        ret_x = self.x
        ret_y = self.y
        action = ""
        if position == "left":
            ret_x = self.x - 1
            action = "left"

        elif position == "right":
            ret_x = self.x + 1
            action = "right"

        elif position == "up":
            ret_y = self.y - 1
            action = "up"

        elif position == "down":
            ret_y = self.y + 1
            action = "down"

        return [ret_x, ret_y, action]


class Game:
    def __init__(self, game_matrix):
        self.game_matrix = game_matrix
        self.dots = calculate_dots(game_matrix)
        self.playable = True

    def whats_at_position(self, x, y):
        return self.game_matrix[y][x]

    def eat_dot(self, x, y):
        if self.game_matrix[y][x] == ".":
            self.game_matrix[y][x] = "#"
            self.dots -= 1
        else:
            print("Cannot eat blank")

    def check_all_dots_eaten(self):
        if self.dots == 0:
            self.playable = False  # the game has ended!
            # print("All dots are eaten")
        else:
            pass

    def print_current_table(self):
        for row in self.game_matrix:
            print(row)
            print("\n")


class Pacman:
    def __init__(self, game_matrix):
        self.game = Game(game_matrix)
        self.player = Player(1, 1)

    def play_game(self):
        self.game.check_all_dots_eaten()
        if not self.game.playable:
            print("Nothing to do here")
        else:
            if self.game.whats_at_position(self.player.x, self.player.y) == ".":
                self.game.eat_dot(self.player.x, self.player.y)
                self.game.check_all_dots_eaten()

            while self.game.playable:
                self.choose_successor_state(self.successor())
                # print(f"Remaining dots: {self.game.dots}")

    def successor(self):
        """Definira funkcija sledbenik odnosno vo koja sostojba moze da se najdam  od momentalnata i so koja akcija"""
        up_coord = self.player.get_coordinates("up")
        down_coord = self.player.get_coordinates("down")
        left_coord = self.player.get_coordinates("left")
        right_coord = self.player.get_coordinates("right")

        actions_coordinates = [up_coord, down_coord, left_coord, right_coord]
        successor_states = {}

        """popolnuvanje . - tocki za jadenje"""

        for action_coord in actions_coordinates:
            # print(f"{action_coord[0]}, {action_coord[1]}")

            if self.game.whats_at_position(action_coord[0], action_coord[1]) == ".":
                successor_states[action_coord[2]] = [action_coord[0], action_coord[1]]

        """popolnuvanje # - prazni mesta"""
        if len(successor_states) == 0:
            for action_coord in actions_coordinates:
                if self.game.whats_at_position(action_coord[0], action_coord[1]) == "#":
                    successor_states[action_coord[2]] = [action_coord[0], action_coord[1]]

        return successor_states

    def choose_successor_state(self, possible_states):
        actions = list(possible_states.keys())

        if len(actions) == 1:
            x = possible_states[actions[0]][0]
            y = possible_states[actions[0]][1]
            """Napravi ja ednata i edinstvena akcija"""
            if self.game.whats_at_position(x, y) == ".":
                self.player.move(actions[0])
                self.game.eat_dot(x, y)
                self.game.check_all_dots_eaten()

            elif self.game.whats_at_position(x, y) == "#":
                self.player.move(actions[0])

        else:
            """Odberi random akcija"""
            action_number = randrange(len(actions))

            x = possible_states[actions[action_number]][0]
            y = possible_states[actions[action_number]][1]

            if self.game.whats_at_position(x, y) == ".":
                self.player.move(actions[action_number])
                self.game.eat_dot(x, y)
                self.game.check_all_dots_eaten()

            elif self.game.whats_at_position(x, y) == "#":
                self.player.move(actions[action_number])


def read_matrix(M, N):
    return_matrix = []
    return_matrix.append(generate_border(N, "!"))
    for i in range(0, M):
        row = list(input())
        row.insert(0, "!")
        row.append("!")
        if len(row) != N + 2:
            print("ERROR")
        return_matrix.append(row)

    return_matrix.append(generate_border(N, "!"))
    return return_matrix


def generate_border(N, delimiter):
    border = list()
    for i in range(0, N + 2):
        border.append(delimiter)
    return border


def calculate_dots(matrix):
    dots_counter = 0
    for item in list(item for row in matrix for item in row):
        if item == ".":
            dots_counter += 1
    return dots_counter


def main():
    M = int(input())
    N = int(input())

    pacman_game = Pacman(read_matrix(M, N))
    pacman_game.play_game()


main()
