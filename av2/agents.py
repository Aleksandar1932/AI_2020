class Agent:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        pass

    def __repr__(self):
        return f"Position of Agent: ({self.x}, {self.y})"


class LeftAgent(Agent):
    def __init__(self, x, y):
        super().__init__(x, y)

    def move(self):
        self.x -= 1


class RightAgent(Agent):
    def __init__(self, x, y):
        super().__init__(x, y)

    def move(self):
        self.x += 1


class UpAgent(Agent):
    def __init__(self, x, y):
        super().__init__(x, y)

    def move(self):
        self.y += 1


class DownAgent(Agent):
    def __init__(self, x, y):
        super().__init__(x, y)

    def move(self):
        self.y -= 1


# Driver code:

if __name__ == '__main__':
    print("LeftAgent:")
    la = LeftAgent(3, 4)
    print(la)
    for i in range(5):
        la.move()
        print(f'Step: {i}, {la}')

    print("RightAgent:")
    ra = RightAgent(-2, 3)
    print(ra)
    for i in range(5):
        ra.move()
        print(f'Step: {i}, {ra}')

    print("UpAgent:")
    ua = UpAgent(-2, -3)
    print(ua)
    for i in range(5):
        ua.move()
        print(f'Step: {i}, {ua}')

    print("DownAgent:")
    da = DownAgent(2, 3)
    print(da)
    for i in range(5):
        da.move()
        print(f'Step: {i}, {da}')
