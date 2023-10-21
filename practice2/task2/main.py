import json

def load_data(filename="tasks.json"):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
        return data
    except (json.JSONDecodeError, FileNotFoundError):
        return {"tasks": [], "categories": []}

def save_data(data, filename="tasks.json"):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

def display_tasks(tasks):
    if not tasks:
        print("Нет задач.")
        return

    for _, task in enumerate(tasks, start=1):
        status = "[x]" if task["completed"] else "[ ]"
        print(f"{status} {task['description']} #{task['category']}")

def display_categories(categories):
    print("Доступные категории:")
    for category in categories:
        print(f"- {category}")

def mark_task_as_completed(tasks, task_index):
    if 1 <= task_index <= len(tasks):
        tasks[task_index - 1]["completed"] = True
        print(f"Задача '{tasks[task_index - 1]['description']}' отмечена как выполненная.")
    else:
        print("Некорректный номер задачи.")

def add_task(tasks, categories):
    description = input("Введите описание задачи: ")
    category = input("Введите категорию задачи: ")

    if category not in categories:
        categories.append(category)

    tasks.append({"description": description, "completed": False, "category": category})
    print("Задача успешно добавлена.")

def search_tasks(tasks, query):
    results = [task for task in tasks if query.lower() in task["description"].lower()]
    return results

if __name__ == "__main__":
    data = load_data()
    tasks = data["tasks"]
    categories = data["categories"]

    while True:
        print("\nМеню:")
        print("1. Просмотреть задачи")
        print("2. Отметить задачу как выполненную")
        print("3. Добавить задачу")
        print("4. Просмотреть категории")
        print("5. Поиск задач")
        print("6. Сохранить и выйти")

        choice = input("Выберите действие (1-6): ")

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            display_tasks(tasks)
            task_index = int(input("Введите номер задачи для отметки (0 для отмены): "))
            if task_index != 0:
                mark_task_as_completed(tasks, task_index)
        elif choice == "3":
            add_task(tasks, categories)
        elif choice == "4":
            display_categories(categories)
        elif choice == "5":
            query = input("Введите строку для поиска: ")
            results = search_tasks(tasks, query)
            display_tasks(results)
        elif choice == "6":
            save_data(data)
            print("Данные сохранены. До свидания!")
            break
        else:
            print("Некорректный выбор. Пожалуйста, введите число от 1 до 6.")
