import sys
import connection
import junk
from config import move_text

cursor, connection = connection.to_db()


def ciout():
    sql = """
    SELECT book_id, title, authors.author_name, genres.genre_name, year, isbn
    FROM books
    JOIN authors ON books.author_id = authors.author_id
    JOIN genres ON books.genre_id = genres.genre_id
    """
    cursor.execute(sql)
    books = cursor.fetchall()
    actions = {
        "1": ciout_all,
        "2": ciout_author,
        "3": ciout_genre
    }
    action = junk.check(move_text, actions, books)
    check = input("Чи бажаєте ви отримати текстовий файл з даними? (Дані існуючого файлу видалсяться)\n"
                  "1 - Так, 2 - Ні\n")
    if check == "1":
        textFile_output(books, 1)


def ciout_all(books):
    for book in books:
        print(f"\nID: ", book[0])
        print("Назва книги: ", book[1])
        print("Автор: ", book[2])
        print("Жанр: ", book[3])
        print("Рік видання: ", book[4])
        print("ISBN: ", book[5])
        print("-------------------------------")


def ciout_author(books):
    while True:
        name = input("Введіть ім'я автора, який вас цікавить: ")
        sql = """
        SELECT book_id, title, authors.author_name, genres.genre_name, year, isbn
        FROM books
        JOIN authors ON books.author_id = authors.author_id
        JOIN genres ON books.genre_id = genres.genre_id
        WHERE authors.author_name LIKE %s
        """
        cursor.execute(sql, ("%" + name + "%",))
        books = cursor.fetchall()
        if books:
            print("Книги автора(ів) з ім'ям, що містить '{}'".format(name))
            ciout_all(books)
            break
        elif name == "q" or name == "й":
            connection.close()
            sys.exit()
        else:
            print("Книги автора(ів) з іменем, що містить '{}', не знайдено."
                  "Спобуйте знову, або й/q, для завершення.".format(name))


def ciout_genre(books):
    while True:
        genre = input("Введіть жанр книг, який вас цікавить: ")
        sql = """
        SELECT book_id, title, authors.author_name, genres.genre_name, year, isbn
        FROM books
        JOIN authors ON books.author_id = authors.author_id
        JOIN genres ON books.genre_id = genres.genre_id
        WHERE genres.genre_name LIKE %s
        """
        cursor.execute(sql, ("%" + genre + "%",))
        books = cursor.fetchall()
        if books:
            print("Книги автора(ів) з ім'ям, що містить '{}'".format(genre))
            ciout_all(books)
            break
        elif genre == "q" or genre == "й":
            connection.close()
            sys.exit()
        else:
            print("Книги автора(ів) з іменем, що містить '{}', не знайдено."
                  "Спобуйте знову, або й/q, для завершення.".format(genre))


def textFile_output(x, move):
    while True:
        blokName = input("\nВедіть назву текстового файлу в який будуть занесені дані: ")
        if blokName[-4:] != ".txt":
            blokName = blokName + ".txt"
        if blokName:
            if move == 1:
                junk.file_writing_all(blokName, x)
                break
        else:
            print("Текствого файлу не існує!")
    print(f"\nДані успішно записано у файл {blokName}")
