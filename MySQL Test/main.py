import sys

import book_update
import deleteBook
from config import hello_txt, values
import connection
import add
import genre_author_checkANDadd
import book_output

cursor, connection = connection.to_db()

# Создайте таблицу

cursor.execute("""
    CREATE TABLE IF NOT EXISTS authors (
        author_id  INT AUTO_INCREMENT PRIMARY KEY,
        author_name VARCHAR(255)
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS genres (
        genre_id INT AUTO_INCREMENT PRIMARY KEY,
        genre_name VARCHAR(255)
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        book_id  INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255),
        author_id INT,
        genre_id  INT,
        year INT,
        isbn  VARCHAR(255),
        FOREIGN KEY (author_id) REFERENCES authors(author_id),
        FOREIGN KEY (genre_id) REFERENCES genres(genre_id)
    )
""")

actions = {
    "1": add.new_book,
    "2": book_output.ciout,
    "3": book_update.update,
    "4": deleteBook.delBook
}


def main_func():
    while True:
        function = input(hello_txt)
        if function in actions:
            actions[function]()
        elif function == "q" or function == "й":
            connection.close()
            sys.exit()
        else:
            print("Выберите допустимый вариант (1, 2, 3... или q/й для выхода).")


for genre in values:
    genre_author_checkANDadd.default_genre_add(genre)
main_func()
