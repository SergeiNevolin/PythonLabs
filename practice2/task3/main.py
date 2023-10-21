import json
from colorama import Fore, Style

def load_data(filename="budget_tracker.json"):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
        return data
    except (json.JSONDecodeError, FileNotFoundError):
        return {"transactions": [], "categories": [], "limits": {}}

def save_data(data, filename="budget_tracker.json"):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

def display_transactions(transactions):
    if not transactions:
        print("Нет записей о транзакциях.")
        return

    for index, transaction in enumerate(transactions, start=1):
        amount = transaction["amount"]
        category = transaction["category"]
        description = transaction["description"]
        transaction_type = "Доход" if amount > 0 else "Расход"
        print(f"{index}. {transaction_type}: {description} ({category}), Сумма: {amount}")

def display_categories(categories):
    print("Доступные категории:")
    for category in categories:
        print(f"- {category}")

def display_analytics(transactions, categories):
    print("Аналитика по категориям:")
    for category in categories:
        total_amount = sum(transaction["amount"] for transaction in transactions if transaction["category"] == category)
        print(f"{category}: {total_amount}")

def add_transaction(transactions, categories, limits):
    description = input("Введите описание операции: ")
    category = input("Введите категорию операции: ")

    if category not in categories:
        print("Такой категории нет. Добавим ее.")
        categories.append(category)
        limits[category] = float(input(f"Установите лимит для категории '{category}': "))

    amount = float(input("Введите сумму операции: "))
    transactions.append({"description": description, "amount": amount, "category": category})
    print("Операция успешно добавлена.")

def check_limits(transactions, limits):
    for category, limit in limits.items():
        total_amount = sum(transaction["amount"] for transaction in transactions if transaction["category"] == category)
        if total_amount > limit:
            print(f"Внимание! Превышен лимит по категории '{category}'. Лимит: {limit}, Расход: {total_amount}")

if __name__ == "__main__":
    data = load_data()
    transactions = data["transactions"]
    categories = data["categories"]
    limits = data["limits"]

    while True:
        print("\nМеню:")
        print("1. Просмотреть транзакции")
        print("2. Добавить транзакцию")
        print("3. Просмотреть категории")
        print("4. Аналитика по категориям")
        print("5. Проверить лимиты по категориям")
        print("6. Сохранить и выйти")

        choice = input("Выберите действие (1-6): ")

        if choice == "1":
            display_transactions(transactions)
        elif choice == "2":
            add_transaction(transactions, categories, limits)
        elif choice == "3":
            display_categories(categories)
        elif choice == "4":
            display_analytics(transactions, categories)
        elif choice == "5":
            check_limits(transactions, limits)
        elif choice == "6":
            save_data(data)
            print("Данные сохранены. До свидания!")
            break
        else:
            print("Некорректный выбор. Пожалуйста, введите число от 1 до 6.")
