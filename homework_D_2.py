import math
from decimal import Decimal, ROUND_HALF_UP


class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        area1 = round(
            self.height * self.width,
        )
        area2 = Decimal(area1).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        return area2

    def diagonal(self):
        a = self.height**2 + self.width**2
        return round(math.sqrt(a), 2)


if __name__ == "__main__":

    rectangle1 = Rectangle(height=5, width=6)
    print(rectangle1.area())  # 30.00
    print(rectangle1.diagonal())  # 7.81

    rectangle2 = Rectangle(height=3, width=3)
    print(rectangle2.area())  # 9.00
    print(rectangle2.diagonal())  # 4.24
