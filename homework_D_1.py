import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(self.radius * self.radius * math.pi, 2)

    def perimeter(self):
        return round(2 * math.pi * self.radius, 2)


if __name__ == "__main__":

    # # 半径1の円
    circle1 = Circle(radius=1)
    print(circle1.area())  # 3.14
    print(circle1.perimeter())  # 6.28

    # # 半径3の円
    circle3 = Circle(radius=3)
    print(circle3.area())  # 28.27
    print(circle3.perimeter())  # 18.85
