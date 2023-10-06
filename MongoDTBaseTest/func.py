import sys
import pymongo
import colorama
import random

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["testDB"]
collection = db["Library"]


def set_random_text_color():
    available_colors = [
        colorama.Fore.RED,
        colorama.Fore.GREEN,
        colorama.Fore.YELLOW,
        colorama.Fore.BLUE,
        colorama.Fore.MAGENTA,
        colorama.Fore.CYAN,
        colorama.Fore.WHITE,
    ]
    x = random.choice(available_colors)
    return x


def contains_numbers(input_string):
    return any(char.isdigit() for char in input_string)


def contains_only_digits(input_string):
    return input_string.isdigit()


def string_check(string):
    color = set_random_text_color()
    y = 0
    while True:
        if y == 1:
            string = input(f"{color}Попробуйте снова: ")
        y = 1
        if contains_numbers(string):
            print("Строка содержит числа. Пожалуйста, введите строку без букв.")
        elif string == "q" or string == "й":
            sys.exit()
        else:
            return string


def numbers_check(string):
    color = set_random_text_color()
    y = 0
    while True:
        if y == 1:
            string = input(f"{color}Попробуйте снова: ")
        y = 1
        if not contains_only_digits(string):
            print("Строка содержит числа. Пожалуйста, введите строку без чисел.")
        elif string == "q" or string == "й":
            sys.exit()
        else:
            return string


def soup(title, author, year, genre, isbn):
    data = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "isbn": isbn
    }
    return data


def name_find():
    color = set_random_text_color()
    name = input(f"{color}Введите интересующее название книги: ")
    find = {
        "$or": [
            {"title": {"$regex": name, "$options": "i"}},
        ]
    }
    print("-------------------------------")
    print("Результаты поиска по запросу: ", name)
    name = collection.find(find)
    if name:
        for result in name:
            color = set_random_text_color()
            print(f"{color}ID: ", result["_id"])
            print("Название книги: ", result["title"])
            print("Автор: ", result["author"])
            print("Год издания: ", result["year"])
            print("Жанр: ", result["genre"])
            print("ISBN: ", result["isbn"])
            print("-------------------------------")
    else:
        print("Книги не найдено")


def author_find():
    color = set_random_text_color()
    name = input(f"{color}Введите интересующео автора: ")
    find = {
        "$or": [
            {"author": {"$regex": name, "$options": "i"}},
        ]
    }
    print("-------------------------------")
    print("Результаты поиска по запросу: ", name)
    name = collection.find(find)
    if name:
        for result in name:
            color = set_random_text_color()
            print(f"{color}ID: ", result["_id"])
            print("Название книги: ", result["title"])
            print("Автор: ", result["author"])
            print("Год издания: ", result["year"])
            print("Жанр: ", result["genre"])
            print("ISBN: ", result["isbn"])
            print("-------------------------------")
    else:
        print("Книги не найдено")


def wherever():
    color = set_random_text_color()
    name = input(f"{color}Введите то что вас интересует: ")
    find = {
        "$or": [
            {"title": {"$regex": name, "$options": "i"}},
            {"author": {"$regex": name, "$options": "i"}},
            {"year": {"$regex": name, "$options": "i"}},
            {"genre": {"$regex": name, "$options": "i"}},
            {"isbn": {"$regex": name, "$options": "i"}}
        ]
    }
    print("-------------------------------")
    print("Результаты поиска по запросу: ", name)
    name = collection.find(find)
    if name:
        for result in name:
            color = set_random_text_color()
            print(f"{color}ID: ", result["_id"])
            print("Название книги: ", result["title"])
            print("Автор: ", result["author"])
            print("Год издания: ", result["year"])
            print("Жанр: ", result["genre"])
            print("ISBN: ", result["isbn"])
            print("-------------------------------")
    else:
        print("Книги не найдено")


def siout():
    color = set_random_text_color()
    name = input(f"{color}Введите то что вас интересует: ")
    find = {
        "$or": [
            {"title": {"$regex": name, "$options": "i"}},
            {"author": {"$regex": name, "$options": "i"}},
            {"year": {"$regex": name, "$options": "i"}},
            {"genre": {"$regex": name, "$options": "i"}},
            {"isbn": {"$regex": name, "$options": "i"}}
        ]
    }
    print("-------------------------------")
    print("Результаты поиска по запросу: ", name)
    name = collection.find(find)
    id = 0;
    if name:
        for result in name:
            color = set_random_text_color()
            id = id + 1
            print(f"{color}{id}. ID: ", result["_id"])
            print("Название книги: ", result["title"])
            print("Автор: ", result["author"])
            print("Год издания: ", result["year"])
            print("Жанр: ", result["genre"])
            print("ISBN: ", result["isbn"])
            print("-------------------------------")
    else:
        print("Книги не найдено")
    neededID = input("Выберите интересующую книгу 1... : ")
    id1 = 0
    list = {}
    name = collection.find(find)
    for result in name:
        id1 = id1 + 1
        if id1 == int(neededID):
            list["_id"] = result["_id"]
            list["title"] = result["title"]
            list["author"] = result["author"]
            list["year"] = result["year"]
            list["genre"] = result["genre"]
            list["isbn"] = result["isbn"]
    color = set_random_text_color()
    print(f"""{color}Для изменения:
    Названия: 1
    Автор: 2
    Год издания: 3
    Жанр: 4
    ISBN:5""")
    change = {
        "1": change_title,
        "2": change_author,
        "3": change_year,
        "4": change_genre,
        "5": change_isbn
    }
    move = input()
    y = 0
    while True:
        if y == 1:
            move = input()
        y = 1
        if move in change:
            change[move](list)
            break
        elif move == "q" or move == "й":
            sys.exit()
        else:
            print(f"{color}Выберите допустимый вариант (1, 2, 3... или q для выхода).")


def input_task():
    color = set_random_text_color()
    function = input(f"{color}Для того, чтобы добавить данные в базу, введите 1\n"
                     "Для того, чтобы выполнить поиск в базе, введите 2\n"
                     "Для того, чтобы обновить данные в базе, введите 3\n"
                     "Для того, чтобы вывести книги из базы, введите 4\n"
                     "Для того, чтобы удалить книгу из базы, введите 5\n"
                     f"Для того, чтобы прервать выполнение программы введите q:")
    return function


def change_title(x):
    y = input("Введите небходимое значение: ")
    filter = x
    update = {
        "$set": {
            "title": y
        }
    }
    result = collection.update_one(filter, update)
    if result.modified_count == 1:
        print("Complete")
    else:
        print("Элемент не был найден или не был обновлен.")


def change_author(x):
    y = input("Введите небходимое значение: ")
    filter = x
    update = {
        "$set": {
            "author": y
        }
    }
    result = collection.update_one(filter, update)
    if result.modified_count == 1:
        print("Complete")
    else:
        print("Элемент не был найден или не был обновлен.")


def change_year(x):
    y = input("Введите небходимое значение: ")
    filter = x
    update = {
        "$set": {
            "year": y
        }
    }
    result = collection.update_one(filter, update)
    if result.modified_count == 1:
        print("Complete")
    else:
        print("Элемент не был найден или не был обновлен.")


def change_genre(x):
    y = input("Введите небходимое значение: ")
    filter = x
    update = {
        "$set": {
            "genre": y
        }
    }
    result = collection.update_one(filter, update)
    if result.modified_count == 1:
        print("Complete")
    else:
        print("Элемент не был найден или не был обновлен.")


def change_isbn(x):
    y = input("Введите небходимое значение: ")
    filter = x
    update = {
        "$set": {
            "isbn": y
        }
    }
    result = collection.update_one(filter, update)
    if result.modified_count == 1:
        print("Complete")
    else:
        print("Элемент не был найден или не был обновлен.")


def book_delete():
    color = set_random_text_color()
    name = input(f"{color}Введите какую книгу вы планируете удалить: ")
    find = {
        "$or": [
            {"title": {"$regex": name, "$options": "i"}},
            {"author": {"$regex": name, "$options": "i"}},
            {"year": {"$regex": name, "$options": "i"}},
            {"genre": {"$regex": name, "$options": "i"}},
            {"isbn": {"$regex": name, "$options": "i"}}
        ]
    }
    print("-------------------------------")
    print("Результаты поиска по запросу: ", name)
    name = collection.find(find)
    id = 0;
    if name:
        for result in name:
            color = set_random_text_color()
            id = id + 1
            print(f"{color}{id}. ID: ", result["_id"])
            print("Название книги: ", result["title"])
            print("Автор: ", result["author"])
            print("Год издания: ", result["year"])
            print("Жанр: ", result["genre"])
            print("ISBN: ", result["isbn"])
            print("-------------------------------")
    else:
        print("Книги не найдено")
    neededID = input("Уточните запрос, выбрав интересующую... : ")
    id1 = 0
    list = {}
    name = collection.find(find)
    for result in name:
        id1 = id1 + 1
        if id1 == int(neededID):
            list["_id"] = result["_id"]
            list["title"] = result["title"]
            list["author"] = result["author"]
            list["year"] = result["year"]
            list["genre"] = result["genre"]
            list["isbn"] = result["isbn"]
    filter = {"_id": list["_id"]}
    result = collection.delete_one(filter)
    print(f"Удалено {result.deleted_count} документов.")


def end():
    sys.exit()
