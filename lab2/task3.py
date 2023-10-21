class Fruit:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return f"{self.color} {self.name}"

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.color}')"

    def __eq__(self, other):
        if isinstance(other, Fruit):
            return self.name == other.name and self.color == other.color
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if isinstance(other, Fruit):
            return (self.name, self.color) < (other.name, other.color)
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Fruit):
            return (self.name, self.color) > (other.name, other.color)
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Fruit):
            return (self.name, self.color) <= (other.name, other.color)
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Fruit):
            return (self.name, self.color) >= (other.name, other.color)
        return NotImplemented

class Berry(Fruit):
    def __init__(self, name, color, taste):
        super().__init__(name, color)
        self.taste = taste

    def __str__(self):
        return f"{self.color} {self.name} with a {self.taste} taste"

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.color}', '{self.taste}')"

class StoneFruit(Fruit):
    def __init__(self, name, color, seed_type):
        super().__init__(name, color)
        self.seed_type = seed_type

    def __str__(self):
        return f"{self.color} {self.name} with {self.seed_type} seed"

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.color}', '{self.seed_type}')"

if __name__ == "__main__":
    # Пример использования
    apple = Fruit("Apple", "Red")
    blueberry = Berry("Blueberry", "Blue", "Sweet")
    peach = StoneFruit("Peach", "Orange", "Pit")

    # Печать строкового представления объектов
    print(apple)
    print(blueberry)
    print(peach) 

    # Печать repr объектов
    print(repr(apple)) 
    print(repr(blueberry))
    print(repr(peach)) 

    # Сравнение объектов
    apple2 = Fruit("Apple", "Red")
    print(apple == apple2)  # Output: True
    print(blueberry != peach)  # Output: True
