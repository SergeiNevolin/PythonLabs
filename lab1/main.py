zoo = {
  'жираф': ['сосед жирафа слева на карте', 'сосед жирафа справа на карте', 'сосед жирафа сверху на карте', 'сосед жирафа снизу на карте'],
  'манул': ['Медведь-губач', 'Жираф', 'Малая панда', 'Большая панда']
}

def get_animal_neighbours(animal: str):
    return zoo.get(animal)


if __name__ == "__main__":
    animal = input('Введите животное: ')
    
    neighbours = get_animal_neighbours(animal.lower())
    
    if neighbours:
        print("Соседи:", end=' ')
        print(*neighbours, sep=', ')
    else:
        print("Такого животного нет")