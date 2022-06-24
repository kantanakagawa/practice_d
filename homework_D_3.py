import math


class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return round(self.side**2, 2)

    def diagonal(self):
        return round(self.side * math.sqrt(2), 2)


if __name__ == "__main__":

    square1 = Square(side=1.5)
    print(square1.area())  # 2.25
    print(square1.diagonal())  # 2.12

    square2 = Square(side=15)
    print(square2.area())  # 225
    print(square2.diagonal())  # 21.21
