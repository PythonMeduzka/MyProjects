import sys
import connection
from config import update_text
import book_output

cursor, connection = connection.to_db()


def delBook():
    while True:
        title = input("\nВведіть назву книги, яку планєте видалити: ")
        sql = """
                SELECT book_id, title, authors.author_name, genres.genre_name, year, isbn
                FROM books
                JOIN authors ON books.author_id = authors.author_id
                JOIN genres ON books.genre_id = genres.genre_id
                WHERE title LIKE %s
                """
        cursor.execute(sql, ("%" + title + "%",))
        books = cursor.fetchall()
        if books:
            print("Книги з назвою, що містить '{}'".format(title))
            book_output.ciout_all(books)
            break
        elif title == "q" or title == "й":
            connection.close()
            sys.exit()
        else:
            print("Книги з назвою, що містить '{}', не знайдено."
                  "Спобуйте знову, або введіть й/q, для завершення.".format(title))
    delete_sql = "DELETE FROM books WHERE book_id = %s"
    cursor.execute(delete_sql, (books[0][0],))
    connection.commit()
    print("\nКнига успішно видалена!")
