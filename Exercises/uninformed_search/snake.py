import sys


def tree_search(problem, fringe):
    """ Пребарувај низ следбениците на даден проблем за да најдеш цел.
    :param problem: даден проблем
    :type problem: Problem
    :param fringe:  празна редица (queue)
    :type fringe: FIFOQueue or Stack or PriorityQueue
    :return: Node or None
    :rtype: Node
    """
    fringe.append(Node(problem.initial))
    while fringe:
        node = fringe.pop()
        print(node.state)
        if problem.goal_test(node.state):
            return node
        fringe.extend(node.expand(problem))
    return None


def breadth_first_tree_search(problem):
    """Експандирај го прво најплиткиот јазол во пребарувачкото дрво.
    :param problem: даден проблем
    :type problem: Problem
    :return: Node or None
    :rtype: Node
    """
    return tree_search(problem, FIFOQueue())


def depth_first_tree_search(problem):
    """Експандирај го прво најдлабокиот јазол во пребарувачкото дрво.
    :param problem: даден проблем
    :type problem: Problem
    :return: Node or None
    :rtype: Node
    """
    return tree_search(problem, Stack())


"""
Неинформирано пребарување во рамки на граф
Основната разлика е во тоа што овде не дозволуваме јамки, 
т.е. повторување на состојби
"""


def graph_search(problem, fringe):
    """Пребарувај низ следбениците на даден проблем за да најдеш цел.
     Ако до дадена состојба стигнат два пата, употреби го најдобриот пат.
    :param problem: даден проблем
    :type problem: Problem
    :param fringe:  празна редица (queue)
    :type fringe: FIFOQueue or Stack or PriorityQueue
    :return: Node or None
    :rtype: Node
    """
    closed = set()
    fringe.append(Node(problem.initial))
    while fringe:
        node = fringe.pop()
        if problem.goal_test(node.state):
            return node
        if node.state not in closed:
            closed.add(node.state)
            fringe.extend(node.expand(problem))
    return None


def breadth_first_graph_search(problem):
    """Експандирај го прво најплиткиот јазол во пребарувачкиот граф.
    :param problem: даден проблем
    :type problem: Problem
    :return: Node or None
    :rtype: Node
    """
    return graph_search(problem, FIFOQueue())


def depth_first_graph_search(problem):
    """Експандирај го прво најдлабокиот јазол во пребарувачкиот граф.
    :param problem: даден проблем
    :type problem: Problem
    :return: Node or None
    :rtype: Node
    """
    return graph_search(problem, Stack())


def depth_limited_search(problem, limit=50):
    """Експандирај го прво најдлабокиот јазол во пребарувачкиот граф
    со ограничена длабочина.
    :param problem: даден проблем
    :type problem: Problem
    :param limit: лимит за длабочината
    :type limit: int
    :return: Node or None
    :rtype: Node
    """

    def recursive_dls(node, problem, limit):
        """Помошна функција за depth limited"""
        cutoff_occurred = False
        if problem.goal_test(node.state):
            return node
        elif node.depth == limit:
            return 'cutoff'
        else:
            for successor in node.expand(problem):
                result = recursive_dls(successor, problem, limit)
                if result == 'cutoff':
                    cutoff_occurred = True
                elif result is not None:
                    return result
        if cutoff_occurred:
            return 'cutoff'
        return None

    return recursive_dls(Node(problem.initial), problem, limit)


def iterative_deepening_search(problem):
    """Експандирај го прво најдлабокиот јазол во пребарувачкиот граф
    со ограничена длабочина, со итеративно зголемување на длабочината.
    :param problem: даден проблем
    :type problem: Problem
    :return: Node or None
    :rtype: Node
    """
    for depth in range(sys.maxsize):
        result = depth_limited_search(problem, depth)
        if result is not 'cutoff':
            return result


def uniform_cost_search(problem):
    """Експандирај го прво јазолот со најниска цена во пребарувачкиот граф.
    :param problem: даден проблем
    :type problem: Problem
    :return: Node or None
    :rtype: Node
    """
    return graph_search(problem, PriorityQueue(min, lambda a: a.path_cost))


import bisect

"""
Дефинирање на класа за структурата на проблемот кој ќе го решаваме со пребарување.
Класата Problem е апстрактна класа од која правиме наследување за дефинирање на основните 
карактеристики на секој проблем што сакаме да го решиме
"""


class Problem:
    def __init__(self, initial, goal=None):
        self.initial = initial
        self.goal = goal

    def successor(self, state):
        """За дадена состојба, врати речник од парови {акција : состојба}
        достапни од оваа состојба. Ако има многу следбеници, употребете
        итератор кој би ги генерирал следбениците еден по еден, наместо да
        ги генерирате сите одеднаш.

        :param state: дадена состојба
        :return:  речник од парови {акција : состојба} достапни од оваа
                  состојба
        :rtype: dict
        """
        raise NotImplementedError

    def actions(self, state):
        """За дадена состојба state, врати листа од сите акции што може да
        се применат над таа состојба

        :param state: дадена состојба
        :return: листа на акции
        :rtype: list
        """
        raise NotImplementedError

    def result(self, state, action):
        """За дадена состојба state и акција action, врати ја состојбата
        што се добива со примена на акцијата над состојбата

        :param state: дадена состојба
        :param action: дадена акција
        :return: резултантна состојба
        """
        raise NotImplementedError

    def goal_test(self, state):
        """Врати True ако state е целна состојба. Даденава имплементација
        на методот директно ја споредува state со self.goal, како што е
        специфицирана во конструкторот. Имплементирајте го овој метод ако
        проверката со една целна состојба self.goal не е доволна.

        :param state: дадена состојба
        :return: дали дадената состојба е целна состојба
        :rtype: bool
        """
        return state == self.goal

    def path_cost(self, c, state1, action, state2):
        """Врати ја цената на решавачкиот пат кој пристигнува во состојбата
        state2 од состојбата state1 преку акцијата action, претпоставувајќи
        дека цената на патот до состојбата state1 е c. Ако проблемот е таков
        што патот не е важен, оваа функција ќе ја разгледува само состојбата
        state2. Ако патот е важен, ќе ја разгледува цената c и можеби и
        state1 и action. Даденава имплементација му доделува цена 1 на секој
        чекор од патот.

        :param c: цена на патот до состојбата state1
        :param state1: дадена моментална состојба
        :param action: акција која треба да се изврши
        :param state2: состојба во која треба да се стигне
        :return: цена на патот по извршување на акцијата
        :rtype: float
        """
        return c + 1

    def value(self):
        """За проблеми на оптимизација, секоја состојба си има вредност.
        Hill-climbing и сличните алгоритми се обидуваат да ја максимизираат
        оваа вредност.

        :return: вредност на состојба
        :rtype: float
        """
        raise NotImplementedError


"""
Дефинирање на класата за структурата на јазел од пребарување.
Класата Node не се наследува
"""


class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        """Креирај јазол од пребарувачкото дрво, добиен од parent со примена
        на акцијата action

        :param state: моментална состојба (current state)
        :param parent: родителска состојба (parent state)
        :param action: акција (action)
        :param path_cost: цена на патот (path cost)
        """
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0  # search depth
        if parent:
            self.depth = parent.depth + 1

    def __repr__(self):
        return "<Node %s>" % (self.state,)

    def __lt__(self, node):
        return self.state < node.state

    def expand(self, problem):
        """Излистај ги јазлите достапни во еден чекор од овој јазол.

        :param problem: даден проблем
        :return: листа на достапни јазли во еден чекор
        :rtype: list(Node)
        """

        return [self.child_node(problem, action)
                for action in problem.actions(self.state)]

    def child_node(self, problem, action):
        """Дете јазел

        :param problem: даден проблем
        :param action: дадена акција
        :return: достапен јазел според дадената акција
        :rtype: Node
        """
        next_state = problem.result(self.state, action)
        return Node(next_state, self, action,
                    problem.path_cost(self.path_cost, self.state,
                                      action, next_state))

    def solution(self):
        """Врати ја секвенцата од акции за да се стигне од коренот до овој јазол.

        :return: секвенцата од акции
        :rtype: list
        """
        return [node.action for node in self.path()[1:]]

    def solve(self):
        """Врати ја секвенцата од состојби за да се стигне од коренот до овој јазол.

        :return: листа од состојби
        :rtype: list
        """
        return [node.state for node in self.path()[0:]]

    def path(self):
        """Врати ја листата од јазли што го формираат патот од коренот до овој јазол.

        :return: листа од јазли од патот
        :rtype: list(Node)
        """
        x, result = self, []
        while x:
            result.append(x)
            x = x.parent
        result.reverse()
        return result

    """Сакаме редицата од јазли кај breadth_first_search или 
    astar_search да не содржи состојби - дупликати, па јазлите што
    содржат иста состојба ги третираме како исти. [Проблем: ова може
    да не биде пожелно во други ситуации.]"""

    def __eq__(self, other):
        return isinstance(other, Node) and self.state == other.state

    def __hash__(self):
        return hash(self.state)


"""
Дефинирање на помошни структури за чување на листата на генерирани, но непроверени јазли
"""


class Queue:
    """Queue е апстрактна класа / интерфејс. Постојат 3 типа:
        Stack(): Last In First Out Queue (стек).
        FIFOQueue(): First In First Out Queue (редица).
        PriorityQueue(order, f): Queue во сортиран редослед (подразбирливо,од најмалиот кон
                                 најголемиот јазол).
    """

    def __init__(self):
        raise NotImplementedError

    def append(self, item):
        """Додади го елементот item во редицата

        :param item: даден елемент
        :return: None
        """
        raise NotImplementedError

    def extend(self, items):
        """Додади ги елементите items во редицата

        :param items: дадени елементи
        :return: None
        """
        raise NotImplementedError

    def pop(self):
        """Врати го првиот елемент од редицата

        :return: прв елемент
        """
        raise NotImplementedError

    def __len__(self):
        """Врати го бројот на елементи во редицата

        :return: број на елементи во редицата
        :rtype: int
        """
        raise NotImplementedError

    def __contains__(self, item):
        """Проверка дали редицата го содржи елементот item

        :param item: даден елемент
        :return: дали queue го содржи item
        :rtype: bool
        """
        raise NotImplementedError


class Stack(Queue):
    """Last-In-First-Out Queue."""

    def __init__(self):
        self.data = []

    def append(self, item):
        self.data.append(item)

    def extend(self, items):
        self.data.extend(items)

    def pop(self):
        return self.data.pop()

    def __len__(self):
        return len(self.data)

    def __contains__(self, item):
        return item in self.data


class FIFOQueue(Queue):
    """First-In-First-Out Queue."""

    def __init__(self):
        self.data = []

    def append(self, item):
        self.data.append(item)

    def extend(self, items):
        self.data.extend(items)

    def pop(self):
        return self.data.pop(0)

    def __len__(self):
        return len(self.data)

    def __contains__(self, item):
        return item in self.data


class PriorityQueue(Queue):
    """Редица во која прво се враќа минималниот (или максималниот) елемент
    (како што е определено со f и order). Оваа структура се користи кај
    информирано пребарување"""
    """"""

    def __init__(self, order=min, f=lambda x: x):
        """
        :param order: функција за подредување, ако order е min, се враќа елементот
                      со минимална f(x); ако order е max, тогаш се враќа елементот
                      со максимална f(x).
        :param f: функција f(x)
        """
        assert order in [min, max]
        self.data = []
        self.order = order
        self.f = f

    def append(self, item):
        bisect.insort_right(self.data, (self.f(item), item))

    def extend(self, items):
        for item in items:
            bisect.insort_right(self.data, (self.f(item), item))

    def pop(self):
        if self.order == min:
            return self.data.pop(0)[1]
        return self.data.pop()[1]

    def __len__(self):
        return len(self.data)

    def __contains__(self, item):
        return any(item == pair[1] for pair in self.data)

    def __getitem__(self, key):
        for _, item in self.data:
            if item == key:
                return item

    def __delitem__(self, key):
        for i, (value, item) in enumerate(self.data):
            if item == key:
                self.data.pop(i)


def move_down(snake, green, red):
    snake_list = list(
        snake)  # nikogash ne pravi prefrlanje na cela lista i site elementi vo torka i obratno, zahtevna operacija e
    green_list = list(green)
    red_list = list(red)

    # y - 1
    curr_head = snake_list[-1]
    curr_x = curr_head[0]
    curr_y = curr_head[1]

    if curr_y - 1 >= 0 and (curr_x, curr_y - 1) not in red_list and (
            curr_x, curr_y - 1) not in snake_list:  # mesto da proveruvash dali sodrzi lista element proveri si torka
        new_head = (curr_x, curr_y - 1)  # faleshe proverka dali zmijata si jade del od teloto
        if new_head in green_list:
            green_list.remove(new_head)
            snake_list.append(new_head)
        else:
            snake_list = snake_list[1:]
            snake_list.append(new_head)

    return tuple(snake_list), tuple(green_list)


def move_up(snake, green, red):
    snake_list = list(snake)
    green_list = list(green)
    red_list = list(red)

    # y - 1
    curr_head = snake_list[-1]
    curr_x = curr_head[0]
    curr_y = curr_head[1]

    if curr_y + 1 < 10 and (curr_x, curr_y + 1) not in red_list and (curr_x, curr_y + 1) not in snake_list:
        new_head = (curr_x, curr_y + 1)
        if new_head in green_list:
            green_list.remove(new_head)
            snake_list.append(new_head)
        else:
            snake_list = snake_list[1:]
            snake_list.append(new_head)

    return tuple(snake_list), tuple(green_list)


def move_right(snake, green, red):
    snake_list = list(snake)
    green_list = list(green)
    red_list = list(red)

    # x + 1
    curr_head = snake_list[-1]
    curr_x = curr_head[0]
    curr_y = curr_head[1]

    if curr_x + 1 < 10 and (curr_x + 1, curr_y) not in red_list and (curr_x + 1, curr_y) not in snake_list:
        new_head = (curr_x + 1, curr_y)
        if new_head in green_list:
            green_list.remove(new_head)
            snake_list.append(new_head)
        else:
            snake_list = snake_list[1:]
            snake_list.append(new_head)

    return tuple(snake_list), tuple(green_list)


def move_left(snake, green, red):
    snake_list = list(snake)
    green_list = list(green)
    red_list = list(red)

    # x - 1
    curr_head = snake_list[-1]
    curr_x = curr_head[0]
    curr_y = curr_head[1]

    if curr_x - 1 >= 0 and (curr_x - 1, curr_y) not in red_list and (curr_x - 1, curr_y) not in snake_list:
        new_head = (curr_x - 1, curr_y)
        if new_head in green_list:
            green_list.remove(new_head)
            snake_list.append(new_head)
        else:
            snake_list = snake_list[1:]
            snake_list.append(new_head)

    return tuple(snake_list), tuple(green_list)


class Snake(Problem):

    def __init__(self, initial, red, goal=None):
        super().__init__(initial, goal)
        self.red = red

    def successor(self, state):
        successor = {}
        red = self.red
        curr_snake = state[0]
        curr_direction = state[1]
        curr_green = state[2]

        # ProdolzhiPravo:
        if curr_direction == "S":
            new_direction = curr_direction
            new_snake, new_green = move_down(curr_snake, curr_green, red)
            if new_snake != curr_snake:
                successor["ProdolzhiPravo"] = (new_snake, new_direction, new_green)

        elif curr_direction == "N":
            new_direction = curr_direction
            new_snake, new_green = move_up(curr_snake, curr_green, red)
            if new_snake != curr_snake:
                successor["ProdolzhiPravo"] = (new_snake, new_direction, new_green)

        elif curr_direction == "E":
            new_direction = curr_direction
            new_snake, new_green = move_right(curr_snake, curr_green, red)
            if new_snake != curr_snake:
                successor["ProdolzhiPravo"] = (new_snake, new_direction, new_green)

        elif curr_direction == "W":
            new_direction = curr_direction
            new_snake, new_green = move_left(curr_snake, curr_green, red)
            if new_snake != curr_snake:
                successor["ProdolzhiPravo"] = (new_snake, new_direction, new_green)

        # SvrtiDesno
        if curr_direction == "S":
            new_direction = "W"
            new_snake, new_green = move_left(curr_snake, curr_green, red)
            if new_snake != curr_snake:
                successor["SvrtiDesno"] = (new_snake, new_direction, new_green)

        elif curr_direction == "N":
            new_direction = "E"
            new_snake, new_green = move_right(curr_snake, curr_green, red)
            if new_snake != curr_snake:
                successor["SvrtiDesno"] = (new_snake, new_direction, new_green)

        elif curr_direction == "E":
            new_direction = "S"
            new_snake, new_green = move_down(curr_snake, curr_green, red)
            if new_snake != curr_snake:
                successor["SvrtiDesno"] = (new_snake, new_direction, new_green)

        elif curr_direction == "W":
            new_direction = "N"
            new_snake, new_green = move_up(curr_snake, curr_green, red)
            if new_snake != curr_snake:
                successor["SvrtiDesno"] = (new_snake, new_direction, new_green)

        # SvrtiLevo

        if curr_direction == "S":
            new_direction = "E"
            new_snake, new_green = move_right(curr_snake, curr_green, red)
            if new_snake != curr_snake:
                successor["SvrtiLevo"] = (new_snake, new_direction, new_green)

        elif curr_direction == "N":
            new_direction = "W"
            new_snake, new_green = move_left(curr_snake, curr_green, red)
            if new_snake != curr_snake:
                successor["SvrtiLevo"] = (new_snake, new_direction, new_green)

        elif curr_direction == "E":
            new_direction = "N"
            new_snake, new_green = move_up(curr_snake, curr_green, red)
            if new_snake != curr_snake:
                successor["SvrtiLevo"] = (new_snake, new_direction, new_green)

        elif curr_direction == "W":
            new_direction = "S"
            new_snake, new_green = move_down(curr_snake, curr_green, red)
            if new_snake != curr_snake:
                successor["SvrtiLevo"] = (new_snake, new_direction, new_green)

        return successor

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return len(state[2]) == 0


if __name__ == '__main__':
    snake_initial = ((0, 9), (0, 8), (0, 7))
    snake_direction = "S"

    n = int(input())
    green = tuple(tuple(map(int, input().split(','))) for _ in range(n))
    m = int(input())
    red = tuple(tuple(map(int, input().split(','))) for _ in range(m))

    snake_problem = Snake((snake_initial, snake_direction, green), red)
    print(breadth_first_graph_search(snake_problem).solution())

    # ne treba da pravish main metoda i da ja povikuvash vo main metodata
