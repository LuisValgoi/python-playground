class Point:
    # constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mov(self):
        print(f'move: {self.x}')

    def draw(self):
        print(f'draw: {self.y}')


point_one = Point(1, 2)
point_one.mov()

point_one = Point(3, 4)
point_one.draw()

