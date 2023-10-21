class Object:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Object at ({self.x}, {self.y})"

class MovingObject(Object):
    def __init__(self, x=0, y=0):
        super().__init__(x, y)

    def __str__(self):
        return f"MovingObject at ({self.x}, {self.y})"

    def __add__(self, other):
        if isinstance(other, MovingObject):
            return MovingObject(self.x + other.x, self.y + other.y)
        else:
            raise ValueError("Unsupported operand type")

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

if __name__ == "__main__":
    obj1 = MovingObject(1, 2)
    obj2 = MovingObject(3, 4)

    print(obj1)  # MovingObject at (1, 2)

    obj3 = obj1 + obj2
    print(obj3)  # MovingObject at (4, 6)

    obj3.move(1, 1)
    print(obj3)  # MovingObject at (5, 7)
