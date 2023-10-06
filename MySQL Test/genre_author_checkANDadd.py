import connection

cursor, connection = connection.to_db()


def default_genre_add(x):
    sql = "SELECT COUNT(*) FROM genres WHERE genre_name = %s"  # Правильно
    cursor.execute(sql, (x,))
    count = cursor.fetchone()[0]
    if count == 0:
        sql = "INSERT INTO genres (genre_name) VALUES (%s)"
        cursor.execute(sql, (x,))
        connection.commit()


def add_genre(x):
    sql = "SELECT COUNT(*) FROM genres WHERE genre_name = %s"  #Не правильно
    cursor.execute(sql, (x,))
    count = cursor.fetchone()[0]
    if count == 0:
        sql = "INSERT INTO genres (genre_name) VALUES (%s)"
        cursor.execute(sql, (x,))
        connection.commit()
        last_genre_id = cursor.lastrowid
    else:
        sql = "SELECT genre_id FROM genres WHERE genre_name = %s"
        cursor.execute(sql, (x,))
        last_genre_id = cursor.fetchone()[0]
    return last_genre_id


def add_author(x):
    sql = "SELECT COUNT(*) FROM authors WHERE author_name = %s"
    cursor.execute(sql, (x,))
    count = cursor.fetchone()[0]
    if count == 0:
        sql = "INSERT INTO authors (author_name) VALUES (%s)"
        cursor.execute(sql, (x,))
        connection.commit()
        last_author_id = cursor.lastrowid
    else:
        sql = "SELECT author_id FROM authors WHERE author_name = %s"
        cursor.execute(sql, (x,))
        last_author_id = cursor.fetchone()[0]
    return last_author_id


