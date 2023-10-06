import sys
import connection
from config import update_text
import genre_author_checkANDadd

cursor, connection = connection.to_db()


def update():
    name = input("\nВведіть назву книги, яку хочете знайти: ")
    sql = """
           SELECT book_id, title, authors.author_name, genres.genre_name, year, isbn
           FROM books
           JOIN authors ON books.author_id = authors.author_id
           JOIN genres ON books.genre_id = genres.genre_id
           WHERE title LIKE %s
           """
    cursor.execute(sql, ("%" + name + "%",))
    books = cursor.fetchall()
    while True:
        if books:
            print("Книги з назвою, що містить '{}'".format(name))
            ciout_all_modificated(books)
            break
        elif name == "q" or name == "й":
            connection.close()
            sys.exit()
        else:
            print("Книги з назвою, що містить '{}', не знайдено."
                  "Спобуйте знову, або й/q, для завершення.".format(name))


def ciout_all_modificated(books):
    for book in books:
        print(f"ID: ", book[0])
        print("Назва книги: ", book[1])
        print("Автор: ", book[2])
        print("Жанр: ", book[3])
        print("Рік видання: ", book[4])
        print("ISBN: ", book[5])
        print("-------------------------------")
    while True:
        id = input("Введіть ID необхідної вам книги: ")
        check = 0
        for book in books:
            if book[0] == int(id):
                print(f"ID: ", book[0])
                print("Назва книги: ", book[1])
                print("Автор: ", book[2])
                print("Жанр: ", book[3])
                print("Рік видання: ", book[4])
                print("ISBN: ", book[5])
                check = 1
                break
        if check != 1:
            print("id Необхідної книги не знайдено. Спробуйте знову.")
        else:
            break

    actions = {
        "1": title_ch,
        "2": author_ch,
        "3": genre_ch,
        "4": year_ch,
        "5": isbn_ch
    }
    while True:
        function = input(update_text)
        if function in actions:
            actions[function](id)
            break
        elif function == "q" or function == "й":
            connection.close()
            sys.exit()
        else:
            print("Виберіть допустимий варіант (1, 2, 3... або q/й для виходу).")


def title_ch(id):
    ch_text = input("Введіть нову назву: ")
    sql = "UPDATE books SET title = %s WHERE book_id = %s"
    values = (ch_text, id)
    cursor.execute(sql, values)
    connection.commit()
    print("\nНазву оновлено оновлено.")


def author_ch(id):
    ch_text = input("Введіть автора: ")
    id_auth = genre_author_checkANDadd.add_author(ch_text)
    sql = "UPDATE books SET author_id = %s WHERE book_id = %s"
    values = (id_auth, id)
    cursor.execute(sql, values)
    connection.commit()
    print("\nАвтора оновлено.")


def genre_ch(id):
    ch_text = input("Введіть новий жанр: ")
    id_genre = genre_author_checkANDadd.add_genre(ch_text)
    sql = "UPDATE books SET genre_id = %s WHERE book_id = %s"
    values = (id_genre, id)
    cursor.execute(sql, values)
    connection.commit()
    print("\nЖанр оновлено.")


def year_ch(id):
    ch_text = input("Введіть новий рік: ")
    sql = "UPDATE books SET year = %s WHERE book_id = %s"
    values = (ch_text, id)
    cursor.execute(sql, values)
    connection.commit()
    print("\nРік оновлено.")


def isbn_ch(id):
    ch_text = input("Введіть новий ISBN: ")
    sql = "UPDATE books SET isbn = %s WHERE book_id = %s"
    values = (ch_text, id)
    cursor.execute(sql, values)
    connection.commit()
    print("\nISBN оновлено.")
