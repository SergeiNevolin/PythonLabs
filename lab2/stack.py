class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not bool(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")

    def size(self):
        return len(self.items)

if __name__ == "__main__":
    stack = Stack()

    # Добавление элементов в стек
    stack.push(1)
    stack.push(2)
    stack.push(3)

    print("Верхний элемент в стеке:", stack.peek())

    removed_item = stack.pop()
    print("Удаленный элемент:", removed_item)

    print("Стек пуст:", stack.is_empty())

    print("Размер стека:", stack.size())
