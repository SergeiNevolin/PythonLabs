import random

# Задача 1
def reverse_list():
    my_list = [random.randint(1, 100) for _ in range(10)]
    print("Исходный список:", my_list)

    reversed_list = my_list[::-1]
    print("Перевернутый список:", reversed_list)

# Задача 2
def combine_lists():
    list1 = [random.randint(1, 100) for _ in range(5)]
    list2 = [random.randint(1, 100) for _ in range(5)]
    print("Список 1:", list1)
    print("Список 2:", list2)

    combined_list = [list1[i] if i % 2 == 0 else list2[i] for i in range(min(len(list1), len(list2)))]
    print("Совмещенный список:", combined_list)

# Задача 3
def remove_duplicates():
    my_list = [random.choice([1, 2, 'a', 'b', 3.14]) for _ in range(10)]
    print("Исходный список:", my_list)

    unique_list = list(set(my_list))
    print("Список без дубликатов:", unique_list)

# Задача 4
def unique_values():
    my_dict = {f'key_{i}': random.choice([random.randint(1, 100), random.randint(1, 4)]) for i in range(5)}
    print("Исходный словарь:", my_dict)

    unique_tuples = [(value, [key for key, val in my_dict.items() if val == value]) for value in set(my_dict.values())]
    print("Кортежи уникальных значений:", unique_tuples)

# Задача 5
def intersection_of_dicts():
    dict1 = {f'key_{i}': random.choice([random.randint(1, 100), random.randint(1, 5)]) for i in range(5)}
    dict2 = {f'key_{i}': random.choice([random.randint(1, 100), random.randint(1, 5)]) for i in range(5)}
    print("Словарь 1:", dict1)
    print("Словарь 2:", dict2)

    intersection_values = set(dict1.values()) & set(dict2.values())

    result_dict = {key: value for key, value in dict1.items() if value in intersection_values}
    print("Новый словарь:", result_dict)

reverse_list()
combine_lists()
remove_duplicates()
unique_values()
intersection_of_dicts()
