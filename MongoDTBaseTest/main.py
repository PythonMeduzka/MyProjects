import pymongo
from colorama import *
import func
import sys

init()

client = pymongo.MongoClient("inputHOST")

db = client["inputDBname"]
collection = db["inputTABLEname"]
reset_color = Style.RESET_ALL


color = func.set_random_text_color()
find_text = f"""{color}
Что бы выполнить поиск по названию введите 1
Что бы выполнить поиск по имени автора введите 2
Не важно - введите 3:
"""


def post_book():
    color = Fore.YELLOW
    title = input(f"{color}Введите название книги: ")
    color = Fore.GREEN
    author = input(f"{color}Введите автора книги: ")
    author = func.string_check(author)
    color = Fore.BLUE
    year = input(f"{color}Введите год издания книги: ")
    year = func.numbers_check(year)
    color = Fore.CYAN
    genre = input(f"{color}Введите жанр книги: ")
    genre = func.string_check(genre)
    isbn = input(f"{color}Введите номер книги: {reset_color}")
    datainput = func.soup(title, author, year, genre, isbn)
    inputData(datainput)


def inputData(data):
    inserted_data = collection.insert_one(data)
    print("ID первого документа: ", inserted_data.inserted_id)


def find_book():
    search_principle = input(find_text)
    principle = {
        "1": func.name_find,
        "2": func.author_find,
        "3": func.wherever
    }
    y = 0
    while True:
        if y == 1:
            search_principle = input()
        y = 1
        if search_principle in principle:
            principle[search_principle]()
            break
        elif search_principle == "q" or search_principle == "й":
            sys.exit()
        else:
            print(f"{color}Выберите допустимый вариант (1, 2, 3 или q для выхода).{reset_color}")


def ciout():
    results = collection.find({})
    while True:
        blokName = input("Ведите название текстового файла в который будут выведены данные: ")
        if blokName[-4:] != ".txt":
            blokName = blokName + ".txt"
        if blokName:
            with open(blokName, "w", encoding="utf-8") as file:
                file.truncate()
                for result in results:
                    file.write(f"ID: {result['_id']}\n")
                    file.write(f"Название книги: {result['title']}\n")
                    file.write(f"Автор: {result['author']}\n")
                    file.write(f"Год издания: {result['year']}\n")
                    file.write(f"Жанр: {result['genre']}\n")
                    file.write(f"ISBN: {result['isbn']}\n")
                    file.write("-------------------------------\n")
                break
        else:
            print("Текствого файла не существует!")

    print(f"Данные успешно записаны в файл {blokName}")


def update_book():
    func.siout()


def delete_book():
    func.book_delete()


actions = {
    "1": post_book,
    "2": find_book,
    "3": update_book,
    "4": ciout,
    "5": delete_book
}
while True:
    function = func.input_task()
    if function in actions:
        actions[function]()
        print(function)
    elif function == "q" or function == "й":
        sys.exit()
    else:
        print(f"{color}Выберите допустимый вариант (1, 2, 3 или q для выхода).{reset_color}")
