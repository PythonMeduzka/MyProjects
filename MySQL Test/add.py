import junk
import genre_author_checkANDadd
import connection

cursor, connection = connection.to_db()


def new_book():
    title = input("Введіть назву книги, яку хочете додати: ")
    author = input("Введіть ім'я та прізвище автора, книгу якого хочете додати: ")
    author = junk.letter_big(author)
    author_id = genre_author_checkANDadd.add_author(author)
    year = input("Введіть рік видання книги, що додається: ")
    genre = input("Введіть жанр видання книги, що додається: ")
    genre_id = genre_author_checkANDadd.add_genre(genre)
    isbn = input("Введіть міжнародний стандартний книжковий номер видання (ISBN) книги, що додається: ")
    sql = "INSERT INTO books (title, author_id, genre_id, year, isbn) VALUES (%s, %s, %s, %s, %s)"
    values = (title, author_id, genre_id, year, isbn)
    cursor.execute(sql, values)
    print("\nКнига успішно додана до бд.")
    connection.commit()
